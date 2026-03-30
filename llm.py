
import requests

def call_llm(prompt):
    try:
        res = requests.post("http://localhost:11434/api/generate", json={
            "model": "mistral",
            "prompt": prompt,
            "stream": False
        })
        return res.json()["response"]
    except:
        return "fallback"

def parse_intent(text):
    prompt = f"Classify intent: {text} -> finance/inventory/insight"
    res = call_llm(prompt).lower()

    if "finance" in res: return "finance"
    if "inventory" in res: return "inventory"
    if "insight" in res: return "insight"
    return "unknown"
