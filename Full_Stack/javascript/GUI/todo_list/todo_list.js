$('#textstuff').keypress(function(e) {
    if (e.which == 13) {  //check if 'Enter' key was pressed
        e.preventDefault();
        addTask();
    }
});

$(document).on('click','#finishBtn', function() {
    finishTask();
});

$(document).on('click','#deleteBtn', function() {
    deleteTask();
});

$(document).on('click','#restoreBtn', function() {
    restoreTask();
});


function addTask() {
    let newSection = document.createElement('section');
    newSection.innerHTML = "" +
        '<textarea readonly class="todoText">' + document.getElementById('textstuff').value + '</textarea>\n' +
        '<button id="finishBtn"> → </button>\n' +
        '<button id="deleteBtn"> X </button>';
    document.getElementById('todoTasks').appendChild(newSection);
    document.getElementById('textstuff').value = '';

    // $('#todoTasks').append('<section></section>');
    // $('#todoTasks section:last-child').append('<textarea>' + $('#textstuff').val() + '</textarea>');
    // $('#todoTasks section:last-child').append('<button onclick="finishTask(this)">✓</button>');
    // $('#todoTasks section:last-child').append('<button onclick="deleteTask(this)">X</button>');
    // $('#textstuff').val('');
}

function finishTask() {
    event.target.parentNode.childNodes[0].className = 'finishText';
    event.target.innerText = '←';
    event.target.id = 'restoreBtn';

    let finishedList = document.getElementById('finishedTasks');
    finishedList.appendChild(event.target.parentNode);
}

function deleteTask() {
    event.target.parentNode.parentNode.removeChild(event.target.parentNode);
}

function restoreTask() {
    event.target.parentNode.childNodes[0].className = 'todoText';
    event.target.innerText = '→';
    event.target.id = 'finishBtn';

    let todoList = document.getElementById('todoTasks');
    todoList.appendChild(event.target.parentNode);
}