let currentMode = "basica";

function setMode(mode) {
    currentMode = mode;
    document.getElementById("extraOptions").innerHTML =
        "<p>Modo selecionado: " + mode + "</p>";
}

function calculate() {
    let expr = document.getElementById("expression").value;
    let output = document.getElementById("output");

    try {

        if (currentMode === "calculo") {
            output.innerText = math.derivative(expr, 'x');
        }

        else {
            output.innerText = math.evaluate(expr);
        }

    } catch {
        output.innerText = "Erro na expressão";
    }
}
