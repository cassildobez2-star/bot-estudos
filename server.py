from flask import Flask, request, jsonify
from flask_cors import CORS
from sympy import symbols, diff, integrate, limit, solve, sympify
from sympy.parsing.sympy_parser import parse_expr

app = Flask(__name__)
CORS(app)  # ⚡ Ativa CORS para aceitar requisições do frontend

x, y, z = symbols('x y z')  # símbolos padrão

@app.route("/")
def home():
    return "MatematicaBC API online 🚀"

@app.route("/calcular", methods=["POST"])
def calcular():
    data = request.json
    modo = data.get("modo")
    expressao = data.get("expressao")
    valor = data.get("valor")  # usado para limite

    try:
        # Converte string para expressão SymPy
        expr = parse_expr(expressao.replace("^","**"))

        if modo == "equacao":
            resultado = solve(expr, x)
        elif modo == "derivada":
            resultado = diff(expr, x)
        elif modo == "integral":
            resultado = integrate(expr, x)
        elif modo == "limite":
            if valor is None or valor == "":
                return jsonify({"erro":"Informe o valor do limite"})
            resultado = limit(expr, x, float(valor))
        else:
            return jsonify({"erro":"Modo inválido"})

        return jsonify({"resultado": str(resultado)})

    except Exception as e:
        return jsonify({"erro": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
