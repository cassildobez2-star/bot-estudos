window.onload = function() {

    window.calculate = function() {

        const expr = document.getElementById("expression").value;
        const output = document.getElementById("output");

        try {
            const result = math.evaluate(expr);
            output.innerText = result;
        } catch (err) {
            output.innerText = "Erro na expressão";
        }
    }

}
