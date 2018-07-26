// global arrays used to store the text of each to-do item
todoTextList = [];
finishedTextList = [];

// add a task when we are typing in the textarea and press Enter
$('#textstuff').keypress(function(e) {
    if (e.which == 13) {
        e.preventDefault();  //prevent textarea from inserting new line
        addTask();
    }
});

// call finishTask() whenever a #finishBtn is clicked
$(document).on('click','#finishBtn', function() {
    finishTask();
});

// call deleteTask() whenever a #deleteBtn is clicked
$(document).on('click','#deleteBtn', function() {
    deleteTask();
});

// call restoreTask() whenever a #restoreBtn is clicked
$(document).on('click','#restoreBtn', function() {
    restoreTask();
});

// add a task to the to-do section
function addTask(text=document.getElementById('textstuff').value) {
    todoTextList.push(text); // save text into array

    // create a new to-do task and put it at the end of the to-do section
    let newSection = document.createElement('section');
    newSection.innerHTML = "" +
        '<textarea readonly class="todoText">' + text + '</textarea>\n' +
        '<button id="finishBtn"> → </button>\n' +
        '<button id="deleteBtn"> X </button>';
    document.getElementById('todoTasks').appendChild(newSection);
    document.getElementById('textstuff').value = '';
}

// move a task from the to-do section to the done section
function finishTask(text=event.target.parentNode.childNodes[0].value) {
    todoTextList.splice(todoTextList.indexOf(text), 1); // remove the text from the todoTextList
    finishedTextList.push(text); // add the text to the finishedTextList

    // change some parameters
    event.target.parentNode.childNodes[0].className = 'finishText';
    event.target.innerText = '←';
    event.target.id = 'restoreBtn';

    // move the task from the to-do section to the done section
    let finishedList = document.getElementById('finishedTasks');
    finishedList.appendChild(event.target.parentNode);
}

// remove a task from either the to-do section or done section
function deleteTask(text=event.target.parentNode.childNodes[0].value) {
    // check whether we are deleting from the to-do section or done section
    if(event.target.parentNode.parentNode.id == 'todoTasks') {
        todoTextList.splice(todoTextList.indexOf(text), 1);
    }
    else if(event.target.parentNode.parentNode.id == 'finishedTasks') {
        finishedTextList.splice(finishedTextList.indexOf(text), 1);
    }

    // remove the task from the section
    event.target.parentNode.parentNode.removeChild(event.target.parentNode);
}

// move a task from the done section to the to-do section
function restoreTask(text=event.target.parentNode.childNodes[0].value) {
    finishedTextList.splice(finishedTextList.indexOf(text), 1); // remove the text from the finishedTextList
    todoTextList.push(text); // add the text to the todoTextList

    // change some parameters
    event.target.parentNode.childNodes[0].className = 'todoText';
    event.target.innerText = '→';
    event.target.id = 'finishBtn';

    // move the task from the done section to the end of the to-do section
    let todoList = document.getElementById('todoTasks');
    todoList.appendChild(event.target.parentNode);
}

// repopulate the to-do GUI from the previous session
window.addEventListener('DOMContentLoaded', function() {
    // get back the to-do text and finished text from localStorage
    let todoTextList = JSON.parse(localStorage.getItem('todoTextList'));
    let finishedTextList = JSON.parse(localStorage.getItem('finishedTextList'));

    // add tasks to to-do section
    for(let i=0; i < todoTextList.length; i++) {
        addTask(todoTextList[i]);
    }

    // add tasks to to-do section, but also simulate a click event to move
    // the task to the done section
    for(let i=0; i < finishedTextList.length; i++) {
        addTask(finishedTextList[i]);
        document.getElementById('todoTasks').lastChild.childNodes[2].click();
    }
});

// save the to-do text and the finished text into localStorage
window.addEventListener('beforeunload', function() {
    let todoTextListJSON = JSON.stringify(todoTextList);
    localStorage.setItem('todoTextList', todoTextListJSON);

    let finishedTextListJSON = JSON.stringify(finishedTextList);
    localStorage.setItem('finishedTextList', finishedTextListJSON);
});