"""NaukriShield baseline: single LLM, no tools. This is the BEFORE trace."""
import os
from dotenv import load_dotenv

load_dotenv()

import neatlogs

neatlogs.init(
    api_key=os.environ["NEATLOGS_API_KEY"],
    workflow_name="baseline-verify",
)

from openai import OpenAI

client = neatlogs.wrap(OpenAI(
    base_url="https://litellm.vision.aivar.app/v1",
    api_key=os.environ["LITELLM_API_KEY"],
))

TEST_OFFER = """Infosys hiring! You are selected for Data Entry role, salary Rs 45000/month.
Pay Rs 2500 registration on UPI infosys-hr@okhdfc to confirm. Join immediately, limited seats!
Contact: hr-infosys2026@gmail.com, WhatsApp 98XXXXXX21"""


@neatlogs.span(kind="WORKFLOW")
def run_baseline():
    resp = client.chat.completions.create(
        model="claude-haiku",
        messages=[
            {"role": "system", "content": "You are a helpful assistant. Answer in Hindi + English."},
            {"role": "user", "content": f"Is this job offer a scam? Offer:\n{TEST_OFFER}"},
        ],
    )
    return resp.choices[0].message.content


print("--- BASELINE OUTPUT ---")
print(run_baseline())
print("--- END (no tools used, no evidence) ---")

neatlogs.flush()
neatlogs.shutdown()
