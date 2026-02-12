from flask import Flask, request, jsonify
from flask_cors import CORS
from sympy import symbols, diff, integrate, limit, solve
from sympy.parsing.sympy_parser import parse_expr
import openai
import os

# ===== Configurações =====
app = Flask(__name__)
CORS(app)  # Permitir chamadas do frontend

# Símbolos padrão
x, y, z = symbols('x y z')

# Chave OpenAI (armazenar como variável de ambiente no Railway)
openai.api_key = os.environ.get("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")

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
        # Substitui ^ por ** e converte para SymPy
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

# ===== IA Chat =====
@app.route("/ia", methods=["POST"])
def ia():
    data = request.json
    pergunta = data.get("pergunta")

    if not pergunta:
        return jsonify({"resposta":"Digite uma pergunta válida."})

    try:
        resposta = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role":"user", "content": pergunta}],
            max_tokens=200
        )
        texto = resposta.choices[0].message.content
        return jsonify({"resposta": texto})

    except Exception as e:
        return jsonify({"resposta": f"Erro IA: {str(e)}"})

# ===== Rodar app =====
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
