function calculate() {
    const expr = document.getElementById("expression").value;
    const output = document.getElementById("output");

    output.innerText = "Você digitou: " + expr;
}
