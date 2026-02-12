let currentMode = "basica";

function setMode(mode) {
    currentMode = mode;
}

function calculate() {
    const expr = document.getElementById("expression").value;
    const output = document.getElementById("output");

    try {

        if (currentMode === "calculo") {
            const derivada = math.derivative(expr, 'x').toString();
            output.innerText = derivada;
        }

        else {
            const resultado = math.evaluate(expr);
            output.innerText = resultado;
        }

    } catch (error) {
        output.innerText = "Erro: expressão inválida";
        console.error(error);
    }
}
