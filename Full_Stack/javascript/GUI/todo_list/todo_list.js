// let addButton = document.getElementById('addBtn');
// if(addButton) {
//     addButton.addEventListener('click', function() {
//         addTask();
//     });
// }
//
// let finishButton = document.getElementById('finishBtn');
// if(finishButton) {
//     console.log('test');
//     finishButton.addEventListener('click', function () {
//         finishTask();
//     });
// }
//
// let deleteButton = document.getElementById('deleteBtn');
// if(deleteButton) {
//     deleteButton.addEventListener('click', function () {
//         deleteTask();
//     });
// }


function addTask() {
    let newSection = document.createElement('section');
    newSection.innerHTML = "" +
        '<textarea >' + document.getElementById('textstuff').value + '</textarea>\n' +
        '<button onclick="finishTask(this)">✓</button>\n' +
        '<button onclick="deleteTask(this)">X</button>';
        // '<button id="finishBtn">✓</button>\n' +
        // '<button id="deleteBtn">X</button>';
    document.getElementById('todoTasks').appendChild(newSection);
    document.getElementById('textstuff').value = '';

    // $('#todoTasks').append('<section></section>');
    // $('#todoTasks section:last-child').append('<textarea>' + $('#textstuff').val() + '</textarea>');
    // $('#todoTasks section:last-child').append('<button onclick="finishTask(this)">✓</button>');
    // $('#todoTasks section:last-child').append('<button onclick="deleteTask(this)">X</button>');
    // $('#textstuff').val('');
}

function finishTask() {
    event.target.parentNode.childNodes[0].style.textDecoration = "line-through";
    event.target.innerText = '↑';
    event.target.onclick = restoreTask;

    let finishedList = document.getElementById('finishedTasks');
    finishedList.appendChild(event.target.parentNode);
}

function deleteTask() {
    event.target.parentNode.parentNode.removeChild(event.target.parentNode);
}

function restoreTask() {
    event.target.parentNode.childNodes[0].style.textDecoration = "none";
    event.target.innerText = '✓';
    event.target.onclick = finishTask;

    let todoList = document.getElementById('todoTasks');
    todoList.appendChild(event.target.parentNode);
}