import os
import requests

API_KEY = os.getenv('OPENAI_API_KEY')

def api_key_available():
    return API_KEY is not None

def get_response(model, prompt, temperature=0.7):
    if not API_KEY:
        raise ValueError("OpenAI API key is not set in the environment variables.")

    url = "https://api.openai.com/v1/engines/{model}/completions".format(model=model)
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": model,
        "prompt": prompt,
        "max_tokens": 150,
        "temperature": temperature
    }

    response = requests.post(url, headers=headers, json=payload)
    response_data = response.json()

    if response.status_code != 200:
        raise ValueError(f"OpenAI API error: {response_data.get('error', {}).get('message', 'Unknown error')}")

    return {
        'text': response_data['choices'][0]['text'],
        'tokens': response_data['usage']['total_tokens']
    }