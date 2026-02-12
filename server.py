HF_TOKEN = os.environ.get("HF_TOKEN")
HF_MODEL = "mistralai/Mistral-7B-Instruct-v0.2"

def gerar_resposta_open_source(pergunta):
    url = f"https://router.huggingface.co/hf-inference/models/{HF_MODEL}"

    headers = {
        "Authorization": f"Bearer {HF_TOKEN}",
        "Content-Type": "application/json"
    }

    payload = {
        "inputs": f"Responda como especialista em matemática:\n{pergunta}",
        "parameters": {
            "max_new_tokens": 200,
            "temperature": 0.5
        }
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code != 200:
        raise Exception(response.text)

    data = response.json()

    if isinstance(data, dict) and "error" in data:
        raise Exception(data["error"])

    return data[0]["generated_text"]
