from flask import Flask, render_template, request, jsonify
import math
import numpy as np
from numpy.polynomial import Polynomial

app = Flask(__name__)

# -------- Funções --------
def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return "Erro! Divisão por zero." if y == 0 else x / y
def exponent(x, y): return x ** y
def square_root(x): return "Erro!" if x < 0 else math.sqrt(x)
def factorial(x): return "Erro!" if x < 0 or not x.is_integer() else math.factorial(int(x))
def trig_sin(x): return math.sin(math.radians(x))
def trig_cos(x): return math.cos(math.radians(x))
def trig_tan(x): return math.tan(math.radians(x))
def trig_asin(x): return "Erro!" if x < -1 or x > 1 else math.degrees(math.asin(x))
def trig_acos(x): return "Erro!" if x < -1 or x > 1 else math.degrees(math.acos(x))
def trig_atan(x): return math.degrees(math.atan(x))

# Matrizes 2x2
def matrix_operations(A, B, op):
    A = np.array(A)
    B = np.array(B)
    if op == "add": return (A + B).tolist()
    if op == "sub": return (A - B).tolist()
    if op == "mul": return np.dot(A, B).tolist()
    if op == "det": return [np.linalg.det(A), np.linalg.det(B)]

# Polinômios
def polynomial_operations(coeffs, x=None, find_roots=False):
    poly = Polynomial(coeffs)
    if find_roots: return poly.roots().tolist()
    return poly(x)

# -------- Rotas --------
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    op = data.get("operation")

    try:
        if op in ["add","sub","mul","div","exp"]:
            x = float(data.get("x"))
            y = float(data.get("y"))
            res = {"add": add, "sub": subtract, "mul": multiply, "div": divide, "exp": exponent}[op](x, y)
        elif op == "sqrt":
            x = float(data.get("x"))
            res = square_root(x)
        elif op == "fact":
            x = float(data.get("x"))
            res = factorial(x)
        elif op == "sin":
            x = float(data.get("x"))
            res = trig_sin(x)
        elif op == "cos":
            x = float(data.get("x"))
            res = trig_cos(x)
        elif op == "tan":
            x = float(data.get("x"))
            res = trig_tan(x)
        elif op == "asin":
            x = float(data.get("x"))
            res = trig_asin(x)
        elif op == "acos":
            x = float(data.get("x"))
            res = trig_acos(x)
        elif op == "atan":
            x = float(data.get("x"))
            res = trig_atan(x)
        elif op == "matrix":
            A = data.get("A") # [[a,b],[c,d]]
            B = data.get("B")
            matOp = data.get("matOp")
            res = matrix_operations(A,B,matOp)
        elif op == "polynomial":
            coeffs = data.get("coeffs")
            x_val = data.get("x")
            find_roots = data.get("roots", False)
            res = polynomial_operations(coeffs, x_val, find_roots)
        else:
            res = "Operação inválida"
    except Exception as e:
        res = f"Erro: {str(e)}"

    return jsonify({"result": res})

if __name__ == "__main__":
    app.run(debug=True)
