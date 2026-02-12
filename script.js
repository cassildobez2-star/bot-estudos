let display = document.getElementById("display");

function append(value) {
    display.value += value;
}

function clearDisplay() {
    display.value = "";
}

function calculate() {
    try {
        let result = math.evaluate(display.value);
        display.value = result;
    } catch (error) {
        display.value = "Erro";
    }
}
