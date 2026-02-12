from flask import Flask, request, jsonify
from flask_cors import CORS
from sympy import symbols, diff, integrate, limit, solve
from sympy.parsing.sympy_parser import parse_expr
import os
import requests

app = Flask(__name__)
CORS(app)

# Símbolos padrão
x, y, z = symbols('x y z')

# Token Hugging Face (adicione no Railway como HF_TOKEN)
HF_TOKEN = os.environ.get("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")
HF_MODEL = "tiiuae/falcon-7b-instruct"

# ===== Rotas =====
@app.route("/")
def home():
    return "MatematicaBC API online 🚀"

# ===== Calculadora =====
@app.route("/calcular", methods=["POST"])
def calcular():
    data = request.json
    modo = data.get("modo")
    expressao = data.get("expressao")
    valor = data.get("valor")

    try:
        expr = parse_expr(expressao.replace("^", "**"))

        if modo == "equacao":
            resultado = solve(expr, x)
        elif modo == "derivada":
            resultado = diff(expr, x)
        elif modo == "integral":
            resultado = integrate(expr, x)
        elif modo == "limite":
            if not valor:
                return jsonify({"erro":"Informe o valor do limite"})
            resultado = limit(expr, x, float(valor))
        else:
            return jsonify({"erro":"Modo inválido"})

        return jsonify({"resultado": str(resultado)})

    except Exception as e:
        return jsonify({"erro": str(e)})

# ===== Função para gerar resposta IA Open-Source =====
def gerar_resposta_open_source(pergunta):
    url = f"https://router.huggingface.co/hf-inference/models/{HF_MODEL}"

    headers = {
        "Authorization": f"Bearer {HF_TOKEN}",
        "Content-Type": "application/json"
    }

    payload = {
        "inputs": pergunta,
        "parameters": {
            "max_new_tokens": 200,
            "temperature": 0.7
        }
    }

    response = requests.post(url, headers=headers, json=payload)
    data = response.json()

    if isinstance(data, dict) and "error" in data:
        raise Exception(data["error"])

    return data[0]["generated_text"]

# ===== Rota Chat IA =====
@app.route("/ia", methods=["POST"])
def ia_open_source():
    data = request.json
    pergunta = data.get("pergunta")
    if not pergunta:
        return jsonify({"resposta":"Digite uma pergunta válida."})

    try:
        texto = gerar_resposta_open_source(pergunta)
        return jsonify({"resposta": texto})
    except Exception as e:
        return jsonify({"resposta": f"Erro IA: {str(e)}"})

# ===== Rodar app =====
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
