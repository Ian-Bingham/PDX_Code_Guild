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

let clockInt = setInterval(clock, 1000);

let time = new Date();
time.setHours(0, 0, 0, 0);
let lapnum = 1;
