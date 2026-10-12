# Demo Video Script — NaukriShield (2:00, read slowly)

## 0:00–0:20 Problem + fake offer (show fixture_fake.txt)
> "Indian students get WhatsApp job offers daily. This one says: Infosys selected you, pay Rs 2,500 on UPI to confirm. Most 12th-pass youth can't tell if it's real. NaukriShield investigates the offer — not just the company — and explains in Hindi."

## 0:20–0:55 Agent investigates (run `python agent.py fixture_fake.txt`, show output)
> "It extracts company, email, UPI, salary. Then it uses tools: Crustdata company and people lookup with cache, domain check — Gmail, not infosys.com — and UPI advance check. Each result decides the next step. Verdict: HIGH RISK, 90. Advance plus Gmail plus UPI plus urgency. What it can't verify, it says unable to verify — never 100% claims."

## 0:55–1:15 Recovery + traces (show neatlogs dashboard, 6 traces)
> "On neatlogs: left is baseline, single LLM with no tools. Right is our agent with extract, tool, and Hindi report spans. I forced a Crustdata timeout — the agent retried once, then finished with a clear limitation. Before versus after, verifiable."

## 1:15–1:35 Entire (show `git log --oneline`, `.entire/settings.json`)
> "On Entire: every commit carries a checkpoint of code plus the agent session, git-refs backend. Judges can review intent, not just code, and search history."

## 1:35–1:55 cfo.ai plan (show cfo-business-plan.xlsx top table)
> "On cfo.ai: cyber-cafes pay Rs 499 a month, API Rs 49 a check, cost Rs 2.25 a check. Year one: 200 cafes plus 30,000 checks is 26.68 lakh revenue, 92.4% margin, break-even at 45 cafes. Assumptions are written in the repo."

## 1:55–2:00 Hindi report + close (show Hindi report + repo link on screen)
> "Final output is Hindi plus English with safe steps and a cybercrime.gov.in and 1930 draft. Repo and evidence are public. Thank you."

### On-screen end card (5 sec)
Repo: https://github.com/adhipatya3552/naukrishield
Traces: neatlogs dashboard | Plan: cfo-business-plan.xlsx | #neatHack
