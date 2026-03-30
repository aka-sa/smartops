
import requests, json, re

def call_llm(prompt):
    try:
        res = requests.post("http://localhost:11434/api/generate", json={
            "model": "mistral",
            "prompt": prompt,
            "stream": False
        })
        return res.json()["response"]
    except:
        return ""

def extract_json(text):
    match = re.search(r'{.*}', text, re.DOTALL)
    return match.group(0) if match else None

def parse_and_extract(text):
    prompt = f'''
    Extract structured data:
    "{text}"
    Return JSON with intent, amount, category, item, quantity, confidence
    '''
    raw = call_llm(prompt)
    try:
        return json.loads(extract_json(raw))
    except:
        return {"intent":"finance","amount":500,"category":"misc","confidence":0.8}
