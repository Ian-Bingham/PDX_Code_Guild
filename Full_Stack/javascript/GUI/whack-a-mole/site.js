no_mole_img_id_list = ['hole1', 'hole2', 'hole3',
    'hole4', 'hole5', 'hole6',
    'hole7', 'hole8', 'hole9'];

let time = new Date();
time.setHours(0, 0, 0, 0);
let timeInt = setInterval(trackTime, 1000);

let int = 1000;
let gameInt = setInterval(popup_mole, int);
let points = 0;
let gameover = false;

// increase the speed that the moles pop up every 10 seconds
function trackTime() {
    time.setSeconds(time.getSeconds() + 1);
    console.log(time.getSeconds());
    if(time.getSeconds() % 10 == 0) {
        clearInterval(gameInt);
        int -= 125;
        gameInt = setInterval(popup_mole, int);
    }
}

function popup_mole() {
    // pick a random img and change it from no_mole to mole
    new_hole_id = no_mole_img_id_list[Math.floor(Math.random() * no_mole_img_id_list.length)];
    $(`#${new_hole_id}`).attr("src", "mole.png");

    // find the hole that we just picked and remove it from the no_mole id list
    let index = no_mole_img_id_list.indexOf(new_hole_id);
    no_mole_img_id_list.splice(index, 1);

    // if the list is empty that means all of the holes have moles. gameover
    if(no_mole_img_id_list.length === 0) {
        $('#lose').show();
        clearInterval(gameInt);
        gameover = true;
    }
}

// if the game is not over alter the points accordingly and display the score
$('img').on('click', function () {
    if(!gameover) {
        if ($(this).attr('src') == 'no_mole.png') {
            points -= 50;
        }
        if ($(this).attr('src') == 'mole.png') {
            points += 100;
            $(this).attr('src', 'no_mole.png');
            no_mole_img_id_list.push($(this).attr('id'));
        }
        $('#score').text(`Points: ${points}`);
    }
});

$('#win_lose').hide();
