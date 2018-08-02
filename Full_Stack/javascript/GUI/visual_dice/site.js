// create div elements for the number of dice the user wants
function createNDice() {
    for(let i=0; i < $('#diceInput').val(); i++) {
        $('#dicesField').append(`<div class="dice" id="dice${i}"></div>`);
    }
}

// rolling for all dice
// randomly generate a number 1-6 and display it in p
function rollNDice() {
    for(let i=0; i < $('#dicesField').children().length; i++) {
        $(`#dice${i}`).text(Math.floor(Math.random() * 6) + 1);
    }
}

// rolling for one dice that is clicked
// randomly generate a number 1-6 and display it in p
function roll() {
    $(event.target).text(Math.floor(Math.random() * 6) + 1);
    $(event.target).animate({backgroundColor: 'green'}, 500, function() {
        $(this).animate({backgroundColor: 'white'}, 500);
    })
}

// go through each dice element, grab the value, and add it to the score
function countScore() {
    let score = 0;
    for(let i=0; i < $('#dicesField').children().length; i++) {
        score += parseInt($(`#dice${i}`).text())
    }
    $('#score').text(`Score: ${score}`);
}

$('#rollBtn').on('click', function() {
    // error checking
    if(isNaN($('#diceInput').val())){
        alert('That was not a number. Please try again.')
    }
    else if($('#diceInput').val() < 1 || $('#diceInput').val() > 50) {
        alert('Please enter a number between 1 and 50.')
    }
    else {
        $('h2').show();
        $('#dicesField').empty();
        createNDice();
        rollNDice();
        countScore();
    }
});


$('#dicesField').on('click', $('.dice'), function() {
    if ($(event.target).is('.dice')) {
        aniDone = false;
        roll();
        countScore();
    }
});

$('h2').hide();