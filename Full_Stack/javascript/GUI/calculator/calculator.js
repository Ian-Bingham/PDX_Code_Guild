const screen = document.getElementById('screen');

document.addEventListener('click', function(event) {
    if (event.target.classList.contains('button')){
        display(event.target);
    }
});

let btClr = document.getElementById('btnClear');
btClr.addEventListener('click', function() {
    clearScreen();
});

let btEq = document.getElementById('btnEq');
btEq.addEventListener('click', function() {
    calculate();
});

function display(button) {
    let buttonText = document.getElementById(button.id).innerText;
    screen.value += `${buttonText}`;
}

function clearScreen() {
    screen.value = '';
}

function calculate() {
    let solution = eval(screen.value);
    clearScreen();
    screen.value = solution;
}
