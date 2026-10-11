"""NaukriShield agent: stateful investigation loop, not fixed pipeline."""
import os
import re
from dotenv import load_dotenv

load_dotenv()

import neatlogs

neatlogs.init(
    api_key=os.environ["NEATLOGS_API_KEY"],
    workflow_name="naukrishield-investigation",
)

from openai import OpenAI
from crustdata_tool import company_lookup, people_lookup

client = neatlogs.wrap(OpenAI(
    base_url="https://litellm.vision.aivar.app/v1",
    api_key=os.environ["LITELLM_API_KEY"],
))
MODEL = "claude-haiku"

FREE_MAIL = {"gmail.com", "yahoo.com", "hotmail.com", "outlook.com"}


@neatlogs.span(kind="AGENT", name="extract")
def extract(text: str) -> dict:
    r = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "Extract JSON only: {company, recruiter, email, domain, upi, salary_monthly, asks_advance(bool), urgency(bool), links[]}"},
            {"role": "user", "content": text[:3000]},
        ],
    )
    import json
    raw = r.choices[0].message.content
    m = re.search(r"\{.*\}", raw, re.S)
    try:
        return json.loads(m.group(0)) if m else {"raw": raw}
    except Exception:
        return {"raw": raw}


@neatlogs.span(kind="TOOL", tool_name="domain_check")
def domain_check(domain: str, company: str):
    if not domain:
        return {"flag": False, "note": "no sender domain found -> cannot verify sender"}
    d = domain.lower()
    if d in FREE_MAIL:
        return {"flag": True, "note": f"free-mail sender {d}, official hiring uses company domain"}
    if company and company.lower().split()[0] not in d:
        return {"flag": True, "note": f"domain {d} does not match claimed company {company}"}
    return {"flag": False, "note": f"domain {d} looks consistent"}


@neatlogs.span(kind="TOOL", tool_name="upi_check")
def upi_check(text: str, facts: dict):
    upi = facts.get("upi") or ("upi" in text.lower() and "found-in-text" or "")
    if facts.get("asks_advance") and upi:
        return {"flag": True, "note": "upfront payment via UPI demanded — top job-scam signal in India"}
    return {"flag": False, "note": "no upfront UPI demand detected"}


@neatlogs.span(kind="WORKFLOW")
def investigate(offer_text: str, max_steps=6):
    evidence, steps = [], []
    facts = extract(offer_text)
    steps.append("extract")
    evidence.append({"tool": "extract", "facts": facts})

    company = facts.get("company", "")
    # Step 2: choose next tool from evidence
    if company:
        for attempt in range(2):  # retry once then fallback
            try:
                c = company_lookup(company)
                evidence.append({"tool": "crustdata_company", "result": c})
                steps.append("crustdata_company")
                break
            except TimeoutError:
                if attempt == 1:
                    evidence.append({"tool": "crustdata_company", "result": {"status": "timeout_after_retry"}})
    # Step 3: people lookup only if recruiter present
    if facts.get("recruiter"):
        p = people_lookup(facts["recruiter"])
        evidence.append({"tool": "crustdata_people", "result": {k: str(v)[:300] for k, v in p.items()}})
        steps.append("crustdata_people")

    # Step 4: deterministic checks (no LLM guessing)
    dc = domain_check(facts.get("domain", ""), company)
    uc = upi_check(offer_text, facts)
    evidence.append({"tool": "domain_check", "result": dc})
    evidence.append({"tool": "upi_check", "result": uc})

    score = 0
    reasons = []
    if facts.get("asks_advance"):
        score += 40
        reasons.append("advance payment demanded (+40)")
    if dc.get("flag"):
        score += 25
        reasons.append(f"sender domain issue (+25): {dc['note']}")
    if uc.get("flag"):
        score += 15
        reasons.append("UPI advance pattern (+15)")
    if facts.get("urgency"):
        score += 10
        reasons.append("urgency pressure (+10)")
    comp = next((e for e in evidence if e["tool"] == "crustdata_company"), None)
    if comp and comp["result"].get("status") in ("timeout", "error", "no_key", "timeout_after_retry"):
        reasons.append("company identity UNABLE TO VERIFY (missing data is not proof of fraud)")

    if score >= 50:
        verdict = "HIGH RISK"
    elif score >= 20:
        verdict = "NEEDS VERIFICATION"
    else:
        verdict = "NO STRONG RED FLAGS FOUND IN CHECKS PERFORMED"
    return {"verdict": verdict, "score": score, "reasons": reasons, "facts": facts, "evidence": evidence, "steps": steps}


@neatlogs.span(kind="AGENT", name="hindi_report")
def hindi_report(inv: dict) -> str:
    r = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "Write short Hindi (Grade 8) + English report. Never claim 100% certainty. If money already sent, mention cybercrime.gov.in + helpline 1930. End with safe next steps + complaint draft outline."},
            {"role": "user", "content": str(inv)[:4000]},
        ],
    )
    return r.choices[0].message.content


if __name__ == "__main__":
    import sys
    text = open(sys.argv[1], encoding="utf-8").read() if len(sys.argv) > 1 else open("fixture_fake.txt", encoding="utf-8").read()
    inv = investigate(text)
    print(f"VERDICT: {inv['verdict']} (score {inv['score']})")
    print("STEPS:", inv["steps"])
    for x in inv["reasons"]:
        print("-", x)
    print("\n--- HINDI REPORT ---\n")
    print(hindi_report(inv))
    neatlogs.flush()
    neatlogs.shutdown()
