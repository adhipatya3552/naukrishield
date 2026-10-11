"""NaukriShield baseline: single LLM, no tools. This is the BEFORE trace."""
import os
from dotenv import load_dotenv

load_dotenv()

try:
    import neatlogs
    neatlogs.init()
    print("neatlogs: init ok")
except Exception as e:
    print(f"neatlogs: skipped ({e})")

from openai import OpenAI

client = OpenAI(
    base_url="https://litellm.vision.aivar.app/v1",
    api_key=os.environ["LITELLM_API_KEY"],
)

TEST_OFFER = """Infosys hiring! You are selected for Data Entry role, salary Rs 45000/month.
Pay Rs 2500 registration on UPI infosys-hr@okhdfc to confirm. Join immediately, limited seats!
Contact: hr-infosys2026@gmail.com, WhatsApp 98XXXXXX21"""

resp = client.chat.completions.create(
    model="claude-haiku",
    messages=[
        {"role": "system", "content": "You are a helpful assistant. Answer in Hindi + English."},
        {"role": "user", "content": f"Is this job offer a scam? Offer:\n{TEST_OFFER}"},
    ],
)
print("--- BASELINE OUTPUT ---")
print(resp.choices[0].message.content)
print("--- END (no tools used, no evidence) ---")
