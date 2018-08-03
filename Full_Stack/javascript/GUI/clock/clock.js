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

    let clock = $('#clock');
    clock.text(`Current Time: ${h}:${m}:${s}`);
}

function startTimer() {
    document.getElementById('timer').style.color = 'black';
    time.setMilliseconds(time.getMilliseconds() + 10);
    [h, m, s, ms] = getTimeIncs(time);

    h = formatTime(h);
    m = formatTime(m);
    s = formatTime(s);
    ms = formatTime(ms / 10);

    $('#timer').text(`${h}:${m}:${s}.${ms}`)
}

function stopTimer() {
    document.getElementById('timer').style.color = 'red';
    clearInterval(timerInt);
}

function resetTimer() {
    document.getElementById('timer').style.color = 'black';
    time.setHours(0, 0, 0, 0);
    $('#timer').text('00:00:00:00');
    $('#laplist').empty();
    lapnum = 1;
}

function lapTimer() {
    $('#laplist').append(`<li>Lap ${lapnum}: ${h}:${m}:${s}.${ms}</li>`);
    lapnum += 1;
}

function convertHours(dlText) {
    let dlTime = new Date();
    dlTime.setHours(dlText, 0, 0, 0);
    return dlTime;
}

function convertMinutes(dlText) {
    let dlTime = new Date();
    let hours = Math.floor(dlText / 60);
    let minutes = dlText % 60;
    dlTime.setHours(hours, minutes, 0, 0);
    return dlTime;
}

function convertSeconds(dlText) {
    let dlTime = new Date();
    let hours = Math.floor(dlText / (60 * 60));
    let minutes = Math.floor(dlText / 60) % 60;
    let seconds = dlText % 60;
    dlTime.setHours(hours, minutes, seconds, 0);
    return dlTime;
}

function convertSimpleDeadline() {
    let dlText = $('#timeInput').val();
    let dlTime = null;
    if($('#cdUnit').val() == 'hoursUnit'){
        dlTime = convertHours(dlText);
    }
    else if($('#cdUnit').val() == 'minutesUnit'){
        dlTime = convertMinutes(dlText);
    }
    else if($('#cdUnit').val() == 'secondsUnit'){
        dlTime = convertSeconds(dlText);
    }

    return dlTime;
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

$('#cdSimpleStartBtn').on('click', function() {
    $('#cdSimpleStartBtn').prop('disabled', true);
    document.getElementById('cdSimpleTime').style.color = 'black';
    console.log($('#cdSimpleTime').text())
    if($('#cdSimpleTime').text() == '00:00:00') {
        dlTime = convertSimpleDeadline();
    }
    else {
        let currDLTime = $('#cdSimpleTime').text();
        let currDLHours = currDLTime.slice(0,2);
        let currDLMinutes = currDLTime.slice(3,5);
        let currDLSeconds = currDLTime.slice(6);
        dlTime.setHours(currDLHours, currDLMinutes, currDLSeconds);
    }

    simpleDeadlineInt = setInterval(function() {
        let dlH = dlTime.getHours();
        let dlM = dlTime.getMinutes();
        let dlS = dlTime.getSeconds();
        if(dlH == 0 && dlM == 0 && dlS == 0) {
            clearInterval(simpleDeadlineInt);
            alert('DONE!!!!!')
        }
        dlTime.setSeconds(dlS - 1);

        $('#cdSimpleTime').text(`${formatTime(dlH)}:${formatTime(dlM)}:${formatTime(dlS)}`)
    }, 1000);

});

$('#cdSimpleStopBtn').on('click', function() {
    $('#cdSimpleStartBtn').prop('disabled', false);
    document.getElementById('cdSimpleTime').style.color = 'red';
    clearInterval(simpleDeadlineInt);
});

$('#cdSimpleResetBtn').on('click', function() {
    document.getElementById('cdSimpleTime').style.color = 'black';
    $('#cdSimpleTime').text('00:00:00');
    dlTime.setHours(0, 0, 0, 0)
});

let clockInt = setInterval(clock, 1000);

let time = new Date();
time.setHours(0, 0, 0, 0);
let lapnum = 1;
