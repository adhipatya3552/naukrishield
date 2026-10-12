# NaukriShield — cfo.ai Business Plan (draft for cfo.ai/neathacks export)
> Status: DRAFT assumptions, no traction claimed. Paste into cfo.ai Ari + export final before submit.

## Pricing
- Students: FREE 3 checks/mo (acquisition)
- Cyber-cafe / coaching centre: Rs 499/mo unlimited counter checks (hero SKU)
- Job portal API: Rs 49/check, Rs 0.40 Lakh/mo minimum

## Costs (per check, LiteLLM hack pricing)
- Extract (claude-haiku ~1.5k tokens): ~Rs 0.40
- Hindi report (claude-haiku ~1.2k tokens): ~Rs 0.35
- Crustdata: 2 lookups cached 70% -> effective ~Rs 1.50 (5000 free credits cover hackathon)
- Infra (Streamlit Cloud free + SQLite): Rs 0
- **Blended cost/check: ~Rs 2.25**

## Revenue (conservative, Year 1)
- 200 cafes x Rs 499 x 12 = Rs 11.98 Lakh
- 30k API checks x Rs 49 x 20% paid mix = Rs 2.94 Lakh
- Total Y1: ~Rs 14.9 Lakh

## Gross margin
- (14.9 - 1.1 costs) / 14.9 = **~92%** (labor excluded, solo founder)

## Runway
- Solo, no salary, hack credits cover inference through Oct. Rs 25k personal buffer = 12+ months to 500 paying counters.
- Break-even: ~45 cafes (Rs 22,455/mo covers Rs 20k infra+API at scale).

## Risks
- Crustdata 403 on hack endpoint (fallback keeps product working, margin holds via cache)
- LiteLLM $20 shared budget -> cap free tier, queue paid
- Never claim accuracy %; verdicts are risk bands + evidence.
