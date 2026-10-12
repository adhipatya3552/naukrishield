"""NaukriShield demo UI: paste offer -> investigation -> Hindi report."""
import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

import neatlogs

neatlogs.init(
    api_key=os.environ["NEATLOGS_API_KEY"],
    workflow_name="naukrishield-investigation",
)

from agent import investigate, hindi_report

st.set_page_config(page_title="NaukriShield — Verify the offer", page_icon="🛡️")
st.title("🛡️ NaukriShield — Verify the offer, not just the company")
st.caption("Paste WhatsApp/Telegram/email job offer (Hindi/English). Evidence-backed, no 100% claims.")

default = open("fixture_fake.txt", encoding="utf-8").read()
text = st.text_area("Job offer text", value=default, height=180)
go = st.button("Investigate")

if go and text.strip():
    with st.spinner("Investigating: extract -> Crustdata -> domain/UPI checks..."):
        inv = investigate(text)
    color = {"HIGH RISK": "red", "NEEDS VERIFICATION": "orange"}.get(inv["verdict"], "green")
    st.markdown(f"### Verdict: :{color}[{inv['verdict']}] (score {inv['score']})")
    st.write("**Steps:**", " → ".join(inv["steps"]))
    with st.expander("Evidence + reasons", expanded=True):
        for r in inv["reasons"]:
            st.write("-", r)
        st.json(inv["facts"])
    st.divider()
    st.markdown(hindi_report(inv))
    st.caption("If money sent: cybercrime.gov.in + helpline 1930. Drafts only, never auto-sent. Missing data = unable to verify, not proof.")
