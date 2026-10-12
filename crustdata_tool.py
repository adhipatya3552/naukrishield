"""Crustdata tools with SQLite cache + failure injection. Real calls when CRUSTDATA_API_KEY present."""
import os
import json
import sqlite3
import urllib.request
import urllib.parse

DB = "crustdata_cache.db"

try:
    import neatlogs
except Exception:
    neatlogs = None

def _span(kind="TOOL", tool_name="crustdata"):
    if neatlogs is None:
        def deco(fn):
            return fn
        return deco
    return neatlogs.span(kind=kind, tool_name=tool_name)

def _db():
    con = sqlite3.connect(DB)
    con.execute("CREATE TABLE IF NOT EXISTS cache (k TEXT PRIMARY KEY, v TEXT)")
    return con

def _get(k):
    con = _db()
    row = con.execute("SELECT v FROM cache WHERE k=?", (k,)).fetchone()
    con.close()
    return json.loads(row[0]) if row else None

def _put(k, v):
    con = _db()
    con.execute("INSERT OR REPLACE INTO cache VALUES (?,?)", (k, json.dumps(v)))
    con.commit()
    con.close()

def _api(path, payload):
    key = os.getenv("CRUSTDATA_API_KEY", "")
    if not key:
        return {"status": "no_key", "note": "CRUSTDATA_API_KEY missing -> UNABLE TO VERIFY, not fraud"}
    if os.getenv("FORCE_CRUSTDATA_TIMEOUT") == "1":
        raise TimeoutError("injected Crustdata timeout (recovery demo)")
    data = json.dumps(payload).encode()
    req = urllib.request.Request(
        f"https://api.crustdata.com{path}", data=data,
        headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=20) as r:
        return json.loads(r.read().decode())

@_span(tool_name="crustdata_company")
def company_lookup(company: str):
    ck = f"company:{company.lower()}"
    hit = _get(ck)
    if hit:
        hit["cached"] = True
        return hit
    try:
        res = _api("/screener/company/search", {"query": company, "page": 1})
        out = {"status": "ok", "raw": str(res)[:2000], "cached": False}
    except TimeoutError as e:
        out = {"status": "timeout", "note": str(e)}
    except Exception as e:
        out = {"status": "error", "note": f"{type(e).__name__}: {e}"[:500]}
    _put(ck, out)
    return out

@_span(tool_name="crustdata_people")
def people_lookup(name: str):
    ck = f"people:{name.lower()}"
    hit = _get(ck)
    if hit:
        hit["cached"] = True
        return hit
    try:
        res = _api("/screener/person/search", {"query": name, "page": 1})
        out = {"status": "ok", "raw": str(res)[:2000], "cached": False}
    except TimeoutError as e:
        out = {"status": "timeout", "note": str(e)}
    except Exception as e:
        out = {"status": "error", "note": f"{type(e).__name__}: {e}"[:500]}
    _put(ck, out)
    return out
