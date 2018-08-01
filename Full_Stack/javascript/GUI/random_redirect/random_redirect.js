// pick a random site and set the iframe src to that site
function chooseRandSite() {
    random_sites = [
        "http://www.neopets.com/",
        "http://www.pog.com/",
        "https://www.oregonhumane.org/",
        "https://t3.rbxcdn.com/4498f0a6eb8db7fc1f698cd690e0f0f2",
        "https://www.khinsider.com/"
    ];

    random_index = Math.floor(Math.random() * random_sites.length);
    $('#frame').attr('src', random_sites[random_index]);
}

// redirect to the random site after 5 seconds
function countDownSeconds() {
    if (seconds == 0) {
        window.location.replace(random_sites[random_index]);
        window.clearInterval(seconds);
    }

    el.innerText = "Redirecting to site in " + seconds + " seconds.";
    seconds -= 1;
}

// pick a different random site when the button is clicked
$('#changeSite').on('click', function() {
    chooseRandSite();
});

let seconds = 5;
let el = document.getElementById('seconds_counter');
let temp = window.setInterval(countDownSeconds, 1000);
chooseRandSite();