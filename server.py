from flask import Flask, request, jsonify
from sympy import *
from sympy.parsing.sympy_parser import parse_expr
from sympy.abc import x, y, z

app = Flask(__name__)

@app.route("/")
def home():
    return "MatematicaBC API online 🚀"

@app.route("/calcular", methods=["POST"])
def calcular():
    data = request.json
    modo = data.get("modo")
    expressao = data.get("expressao")
    valor = data.get("valor")

    try:
        expr = parse_expr(expressao)

        if modo == "equacao":
            resultado = solve(expr, x)

        elif modo == "derivar":
            resultado = diff(expr, x)

        elif modo == "integrar":
            resultado = integrate(expr, x)

        elif modo == "limite":
            resultado = limit(expr, x, float(valor))

        else:
            return jsonify({"erro": "Modo inválido"})

        return jsonify({"resultado": str(resultado)})

    except Exception as e:
        return jsonify({"erro": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
