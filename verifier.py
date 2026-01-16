import requests
import json

def verify_claim(claim, context=None):
    if not context:
        return "unverified", "No context", 0.0

    url = "http://localhost:11434/api/generate"
    
    # Shortened prompt = faster processing
    prompt = f"Context: {context}\nClaim: {claim}\nReturn JSON: {{'verdict': 'true/false', 'reason': 'short', 'conf': 0.9}}"

    try:
        response = requests.post(url, json={
            "model": "llama3.2:1b",
            "prompt": prompt,
            "stream": False,
            "format": "json",
            "options": {
                "num_predict": 50,  # STOP the model from rambling
                "temperature": 0.1   # Keep it focused
            }
        }, timeout=10)
        
        res_data = json.loads(response.json()['response'])
        
        # Safe extraction
        v = str(res_data.get('verdict', 'false')).lower()
        r = res_data.get('reason', 'N/A')
        c = float(res_data.get('conf', 0.7))
        
        return v, r, c
    except:
        return "error", "Local LLM timeout", 0.0