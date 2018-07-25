// calculator.js 7/24/18

while (true) {
    alert("Welcome to Calculator!");
    let operation_list = ['+', '-', '*', '/'];
    let num1 = Number(prompt("Type in your first number."));
    while(isNaN(num1)) {
        alert("That was not a number.");
        num1 = Number(prompt("Type in your first number."));
    }

    let operation = prompt("Type in the operation you would like to perform");
    while(operation_list.indexOf(operation) == -1) {
        alert("Invalid operation.");
        operation = prompt("Type in the operation you would like to perform");
    }

    let num2 = Number(prompt("Type in your second number."));
    while(isNaN(num2)) {
        alert("That was not a number.");
        num2 = Number(prompt("Type in your second number."));
    }

    let solution = 0;

    switch (operation) {
        case '+':
            solution = num1 + num2;
            break;
        case '-':
            solution = num1 - num2;
            break;
        case '*':
            solution = num1 * num2;
            break;
        case '/':
            solution = num1 / num2;
            break;
    }

    alert(`${num1} ${operation} ${num2} = ${solution}`);

    let again = prompt("Again (y or n)?").toLowerCase();
    if (again == 'n' || again == null) {
        break;
    }
}