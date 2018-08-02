// create div elements for the number of dice the user wants
function createNDice() {
    for(let i=0; i < $('#diceInput').val(); i++) {
        $('#dicesField').append(`<div tabindex="${i}" class="dice" id="dice${i}"></div>`);
    }
}

// rolling for all dice
// randomly generate a number 1-6 and display it
function rollNDice() {
    for(let i=0; i < $('#dicesField').children().length; i++) {
        $(`#dice${i}`).text(Math.floor(Math.random() * 6) + 1);
        $(`#dice${i}`).animate({backgroundColor: 'green'}, 300, function() {
            $(`#dice${i}`).animate({backgroundColor: 'white'}, 300, function() {})
        })
    }
}

// rolling for one dice that is clicked
// randomly generate a number 1-6 and display it in p
function roll() {
    $(event.target).text(Math.floor(Math.random() * 6) + 1);
}

function colorAni() {
    // while the color animation is running we want to unbind the click events
    // for each dice so we do not overrun them with multiple clicks,
    // then rebind them when the animation is over
    $('#dicesField').unbind();
    $(event.target).animate({backgroundColor: 'green'}, 300, function() {
        $(this).animate({backgroundColor: 'white'}, 300, function() {
            $('#dicesField').bind('click', $('.dices'), function() {
                if($(event.target).is('.dice')) {
                    colorAni();
                    roll();
                    countScore();
                }
            });
        });
    });
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

// allow user to press enter instead of roll button
$('#diceInput').keypress(function(e) {
    if (e.which == 13) {
        $('#rollBtn').click();
    }
});

// bind this click functionality when the page is loaded
$(document).ready(function() {
    $('#dicesField').bind('click', $('.dice'), function() {
        if($(event.target).is('.dice')) {
            colorAni();
            roll();
            countScore();
        }
    });
});

$('h2').hide();
