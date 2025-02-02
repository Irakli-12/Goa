function calculateSum() {
    var number1 = Number(document.getElementById('number1').value);
    var number2 = Number(document.getElementById('number2').value);
    var sum = number1 + number2;
    document.getElementById('result').textContent = "sum =" + sum;
}