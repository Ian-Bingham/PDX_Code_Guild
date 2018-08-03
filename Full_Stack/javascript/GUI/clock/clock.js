function formatTime(num) {
    if(num < 10) {
        num = '0' + num;
    }
    return num;
}

function getTimeIncs(foo) {
    let hours = foo.getHours();
    let minutes = foo.getMinutes();
    let seconds = foo.getSeconds();
    let milliseconds = foo.getMilliseconds();

    return [hours, minutes, seconds, milliseconds];
}

function clock() {
    let now = new Date();
    let [h, m, s, ms] = getTimeIncs(now);

    m = formatTime(m);
    s = formatTime(s);

    let clock = document.getElementById('clock');
    clock.innerText = 'Current Time: ' + h + ':' + m + ':' + s;
}

function startTimer() {
    document.getElementById('timer').style.color = 'black';
    time.setMilliseconds(time.getMilliseconds() + 10);
    [h, m, s, ms] = getTimeIncs(time);

    h = formatTime(h);
    m = formatTime(m);
    s = formatTime(s);
    ms = formatTime(ms / 10);

    document.getElementById('timer').innerText = h +
        ':' + m +
        ':' + s +
        ':' + ms;
}

function stopTimer() {
    document.getElementById('timer').style.color = 'red';
    clearInterval(timerInt);
}

function resetTimer() {
    document.getElementById('timer').style.color = 'black';
    time.setHours(0, 0, 0, 0);
    document.getElementById('timer').innerText = '00:00:00:00';
    $('#laplist').empty();
    lapnum = 1;
}

function lapTimer() {
    $('#laplist').append(`<li>Lap ${lapnum}: ${h}:${m}:${s}:${ms}</li>`);
    lapnum += 1;
}

function convertHours(deadline) {
    let time = new Date();
    time.setHours(deadline, 0, 0, 0);
    return time;
}

function convertMinutes(deadline) {
    let time = new Date();
    let hours = Math.floor(deadline / 60);
    let minutes = deadline % 60;
    time.setHours(hours, minutes, 0, 0);
    return time;
}

function convertSeconds(deadline) {
    let time = new Date();
    let hours = Math.floor(deadline / (60 * 60));
    let minutes = Math.floor(deadline / 60) % 60;
    let seconds = deadline % 60;
    time.setHours(hours, minutes, seconds, 0);
    return time;
}

function convertSimpleDeadline() {
    let deadline = $('#timeInput').val();
    let time = null;
    if($('#cdUnit').val() == 'hoursUnit'){
        time = convertHours(deadline);
    }
    else if($('#cdUnit').val() == 'minutesUnit'){
        time = convertMinutes(deadline);
    }
    else if($('#cdUnit').val() == 'secondsUnit'){
        time = convertSeconds(deadline);
    }

    simpleDeadlineInt = setInterval(function() {
        if(time.getHours() == 0 &&
            time.getMinutes() == 0 &&
            time.getSeconds() == 0) {
            clearInterval(simpleDeadlineInt);
            alert('DONE!!!!!')
        }
        time.setSeconds(time.getSeconds() - 1);
        $('#cdSimpleTime').text(`${formatTime(time.getHours())}:${formatTime(time.getMinutes())}:${formatTime(time.getSeconds())}`)
    }, 1000);
}

// function getDateDeadline() {
//     let deadline = $('#dateInput').val();
//     let month = deadline.slice(0, 2) - 1; //month index from 0-11
//     let day = deadline.slice(3, 5);
//     let year = deadline.slice(6);
//     return [month, day, year];
// }
//
// function calcMsRemaining() {
//     let now = new Date();
//     msRemaining = deadline - now;
//     if(msRemaining <= 0){
//         clearInterval(countDownInt);
//         $('#countdownDateDone').show();
//     }
//     $('#countdownDateTime').text(msRemaining)
// }

$('#startBtn').on('click', function() {
    timerInt = setInterval(startTimer, 10);
    $('#startBtn').prop('disabled', true);
    $('#stopBtn').prop('disabled', false);
    $('#resetBtn').prop('disabled', true);
    $('#lapBtn').prop('disabled', false);
});

$('#stopBtn').on('click', function() {
    stopTimer();
    $('#startBtn').prop('disabled', false);
    $('#stopBtn').prop('disabled', true);
    $('#resetBtn').prop('disabled', false);
    $('#lapBtn').prop('disabled', false);
});

$('#resetBtn').on('click', function() {
    resetTimer();
    $('#startBtn').prop('disabled', false);
    $('#stopBtn').prop('disabled', true);
    $('#resetBtn').prop('disabled', true);
});

$('#lapBtn').on('click', function() {
    lapTimer();
});

$('#cdSimpleStartBtn').on('click', function() {
    convertSimpleDeadline();
});

// $('#cdSimpleStopBtn').on('click', function() {
//     clearInterval(simpleDeadlineInt);
// });

// $('#cdDateBtn').on('click', function() {
//     let [m, d, y] = getDateDeadline();
//     deadline = new Date(y, m, d);
//     countdownInt = setInterval(calcMsRemaining, 1000);
// });

let clockInt = setInterval(clock, 1000);

let time = new Date();
time.setHours(0, 0, 0, 0);
let lapnum = 1;

// $('#cdDateDone').hide();
