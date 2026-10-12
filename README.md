# 🛡️ NaukriShield — Verify the offer, not just the company

Evidence-backed job-offer investigation agent for Indian job seekers (Hindi/English). Pastes a WhatsApp/Telegram/email offer → investigates → explains evidence → safe next steps.

## Setup (free-tier only)
```
pip install -r requirements.txt
# .env (never commit): LITELLM_API_KEY, CRUSTDATA_API_KEY, NEATLOGS_API_KEY
$env:PYTHONUTF8="1"
python baseline.py                    # BEFORE: single LLM, no tools
python agent.py fixture_fake.txt      # AFTER: full investigation
streamlit run app.py                  # demo UI
```

## Architecture
`Streamlit UI → investigate() WORKFLOW → extract (AGENT/LLM) → Crustdata company/people (TOOL, SQLite cached, retry-once) → domain_check + upi_check (TOOL, deterministic) → weighted rules (40/25/15/10) → HIGH RISK / NEEDS VERIFICATION / NO STRONG RED FLAGS → hindi_report (AGENT/LLM, cybercrime.gov.in + 1930)`

Single stateful orchestrator, not fixed 4-agent pipeline. Missing data = UNABLE TO VERIFY, never proof of fraud/safety.

## Sponsor tools
- **neatlogs:** workflows `baseline-verify` (BEFORE) vs `naukrishield-investigation` (AFTER) + timeout recovery run. Init + wrap + WORKFLOW/AGENT/TOOL spans, flush/shutdown on scripts.
- **Entire:** enabled (`entire enable`, `.entire/settings.json`), checkpoints per commit via git-refs.
- **cfo.ai:** see BUSINESS_PLAN.md (Rs 499/mo cafe hero SKU, ~Rs 2.25/check, ~92% margin, explicit assumptions). Export final from cfo.ai/neathacks before submit.
- **Crustdata:** real Company + People lookups, SQLite cache (70%+ hit), `FORCE_CRUSTDATA_TIMEOUT=1` recovery demo. Current hack endpoint returns HTTP 403 → recorded as error evidence, product falls back honestly (confirm correct endpoint on Discord).

## Tests (verified Oct 12)
- `fixture_fake.txt` (Infosys + UPI advance) → HIGH RISK 90
- `fixture_real.txt` (campus interview, no fee) → NO STRONG RED FLAGS 0
- `fixture_ambiguous.txt` (Sharma Enterprises, no email) → NEEDS VERIFICATION 25
- `FORCE_CRUSTDATA_TIMEOUT=1` → still completes, timeout noted (recovery)

## Limitations
- No 100% certainty claimed; fictionalized fixtures (never accuse real Infosys).
- OCR via pasted text primary (screenshot OCR optional).
- `.env` + `*.db` gitignored; rotate any exposed key.

## Demo (≤3 min)
0:00 problem + fake offer → 0:20 extract + tool calls → 1:05 forced-timeout recovery + traces → 1:35 before/after → 2:00 Entire checkpoint → 2:25 cfo.ai plan → 2:45 Hindi report + repo link.
