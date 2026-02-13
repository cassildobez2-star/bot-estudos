from sympy import symbols, diff, integrate, limit, solve, factorial
from sympy.parsing.sympy_parser import parse_expr
from sympy import binomial

x = symbols('x')

@app.route("/calcular", methods=["POST"])
def calcular():
    data = request.json
    modo = data.get("modo")
    expressao = data.get("expressao")
    valor = data.get("valor")
    n = data.get("n")
    k = data.get("k")

    try:
        if modo == "derivada":
            expr = parse_expr(expressao.replace("^","**"))
            resultado = diff(expr, x)

        elif modo == "integral":
            expr = parse_expr(expressao.replace("^","**"))
            resultado = integrate(expr, x)

        elif modo == "limite":
            expr = parse_expr(expressao.replace("^","**"))
            resultado = limit(expr, x, float(valor))

        elif modo == "equacao":
            expr = parse_expr(expressao.replace("^","**"))
            resultado = solve(expr, x)

        elif modo == "fatorial":
            resultado = factorial(int(n))

        elif modo == "combinacao":
            resultado = binomial(int(n), int(k))

        elif modo == "permutacao":
            resultado = factorial(int(n)) / factorial(int(n)-int(k))

        else:
            return jsonify({"erro":"Modo inválido"})

        return jsonify({"resultado": str(resultado)})

    except Exception as e:
        return jsonify({"erro": str(e)})
