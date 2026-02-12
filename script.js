<script>

let mode = "basica";

function setMode(newMode){
    mode = newMode;
    document.getElementById("output").innerText = "Modo: " + newMode;
}

function calculate() {
    const expr = document.getElementById("expression").value;
    const output = document.getElementById("output");

    try {

        if(mode === "calculo-derivada"){
            output.innerText = math.derivative(expr, 'x').toString();
        }

        else if(mode === "calculo-integral"){
            // Integral numérica simples
            const f = math.compile(expr);
            let sum = 0;
            let a = 0;
            let b = 10;
            let step = 0.01;

            for(let x=a; x<=b; x+=step){
                sum += f.evaluate({x:x}) * step;
            }

            output.innerText = "Integral aproximada (0 a 10): " + sum;
        }

        else {
            output.innerText = math.evaluate(expr);
        }

    } catch(err){
        output.innerText = "Erro na expressão";
    }
}

</script>
