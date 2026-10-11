# neatHack Chat History — NaukriShield Selection
Date: 2026-10-11 | Project: D:\Builds\neathack-project | User: Adhipatya Saxena

## 1. User initial request
- Links: https://neatlogs.com/hackathon, https://luma.com/s5blr882?tk=dVV9hf, https://app.crustdata.com/home, https://entire.io/et/project1/project-1 + screenshot image
- Asked to: read profile + opencode config, research hackathon + sponsor software, use only free-tier tools (no paid), first-principles thinking, detailed breakdown of unique daily-life India ideas, todo list step-by-step, use skills with low consumption, accurate output only.
- Profile rule recalled: `C:\Users\adhip\.config\opencode\PROFILE.md` — B.Tech AI JLU, stack Python/JS/TS/SQL/C++, scikit-learn/Pandas/Numpy/XGBoost/LangChain/LLMs/GenAI/Agentic, Next.js/FastAPI/Tailwind/Streamlit/REST, Git/Docker/Convex/Auth0/Vercel/Qdrant/Vapi/Deepgram/OpenRouter/MySQL/Elasticsearch/Cloudflare Workers. Avoid repeats: LifeOS, NotER, AskProperty, SocialVerify, FinTrack, Trading_Bot, House Price/Churn/Fraud-ML/Spam/RAG-PDF/Resume-Analyzer, court-navigator, AuditMind/RegPilot/LegalEase/PayGuard/ComplianceWatch, PitchAutopsy/NegotiAI, StudyBand/SyllabusAgent/DebateBot/SearchBot, Stock-Monitor, tigergraph-fraud-agent. Each idea must give: problem, why unsolved, edge, exact build, pitch/demo. Daily India problems only.

## 2. Assistant: skill + todos + research
- Invoked `brainstorming` skill. Classified as **architectural** (new agent system, empty workspace).
- Created todos: explore context, research sponsors/judging, clarifying questions, propose ideas, recommendation.
- Read PROFILE.md + empty workspace dir. Fetched:
  - neatlogs.com/hackathon: #neatHack Oct 10-12 2026 online, one track "Build an agent that works (literally)", mandatory neatlogs + Entire + cfo.ai, judging Agent 30% / Tool use 25% / Demo 20% / Building in public 15% / Usefulness 10%, prizes $19k ($2k/$1k/$500 + $500 community + Dodo credits + neatlogs Pro), submit Oct 12 7-11:55 PM IST via X quote-post, public repo commits during hackathon, before/after traces + recovery run required.
  - Luma s5blr882: 1357 going, hosts Ajay Yadav/Simran Sachdeva/Aj, online, registration closed.
  - entire.io: checkpoints per commit + entire-graph, CLI `curl -fsSL https://entire.io/install.sh | bash`, MIT, works with OpenCode.
  - docs.neatlogs.com: `pip install -U neatlogs` + `neatlogs.init()`, wizard `npx @neatlogs/wizard`.
  - crustdata.com/api-documentation: Company + People APIs, 5000 free credits for participants.
  - cfo.ai/neathacks: Ari business modeling, card required then cancel immediately, hack credits provided.

## 3. Clarifying questions
- Asked: Solo vs Team, Text Hindi/English vs +voice.
- User answered: Solo, Text Hindi/English.

## 4. Three ideas proposed
### Idea 1 — NaukriShield (RECOMMENDED)
- Problem: fake job offers on WhatsApp/Telegram asking UPI registration fee.
- Why unsolved: cybercrime portal post-facto English, Crustdata B2B-only, youth needs Hindi screenshot verdict.
- Edge: SocialVerify + Fraud-ML/XGBoost + tigergraph-fraud-agent, new victim-side user.
- Build: Streamlit -> Intake (Tesseract OCR) -> Verifier (Crustdata Company+People + domain/UPI checks) -> Risk (XGBoost rules) -> Action (Hindi explanation + cybercrime draft). SQLite/Qdrant state, LiteLLM hack key, Convex free.
- Pitch: fake Infosys vs real letter side-by-side, RED in Hindi.

### Idea 2 — BijliBill Nyay
- Problem: inflated MPPKVVCL bills, English slabs, lineman pressure.
- Why unsolved: no Hindi math explainer + complaint drafter.
- Edge: FinTrack/PayGuard/EDA/Streamlit.
- Build: meter photo + bill PDF -> Reader -> Slab Calculator (MP rules) -> Dispute Agent -> Watcher.
- Weakness: Crustdata forced, less agent-necessity.

### Idea 3 — Asli Supplier
- Problem: kirana pays advance to fake distributor, goods never come.
- Why unsolved: Khatabook manual, no supplier verification.
- Edge: LifeOS + Trading_Bot pipes + Fraud-ML.
- Build: supplier name/mobile/UPI -> Crustdata Enrichment -> Risk -> Ledger draft.
- Weakness: lower demo emotion than job fraud.

- Free-only first-principles stack listed: LiteLLM $20 key + OpenRouter free fallback, Python/FastAPI/Streamlit or Next.js/Vercel free, LangChain, Qdrant/Convex free, Tesseract/PyMuPDF free, GitHub free, Entire free, neatlogs free, cfo.ai credits, Crustdata 5000 cache+mock.

## 5. User: which problem for Python? First-principles + honest + check .env
- Assistant verified `D:\Builds\neathack-project\.env` exists with `LITELLM_API_KEY` (value redacted here: sk-W3n...3g). Advised .gitignore + os.getenv.
- Honest pick: NaukriShield. Reasons: highest frequency (weekly vs monthly), information asymmetry solvable with Crustdata+LLM Hindi, true agent loop (extract->enrich->reason->act), sponsor-fit natural (Crustdata core), solo 48h Python feasible, small tokens safe on LiteLLM key, clear cfo.ai model (Rs 49/check via cyber-cafe).

## 6. User: yes if best chance to win, go ahead
- Assistant locked NaukriShield, started tight spec todo (architecture, files, evidence plan, Hindi demo).
- Presented Section 1/3 Architecture + 4-agent flow:
  Streamlit -> orchestrator.py -> A1 Intake (OCR+Tesseract+LiteLLM JSON) -> A2 Verifier (Crustdata Company/People + domain/UPI, SQLite cache) -> A3 Risk (deterministic Python+XGBoost 6 features) -> A4 Action (Hindi explainer + refusal + cybercrime draft, drafts only). Hits planning/tool-use/state/context/execution/recovery/verification/iteration.
- Asked for approval to send Section 2.

## 7. User: save whole chat as .md right now
- This file created per request. Secrets redacted. No code implemented yet (brainstorming hard-gate: await design approval).
