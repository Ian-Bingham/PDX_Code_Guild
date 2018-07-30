function randomSite() {
    let random_sites = [
        "https://genius.com/Panic-at-the-disco-hey-look-ma-i-made-it-lyrics",
        "https://www.reddit.com/r/AskReddit/comments/5z4b1u/whats_a_short_clean_joke_that_gets_a_laugh_every/",
        "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        "https://t3.rbxcdn.com/4498f0a6eb8db7fc1f698cd690e0f0f2",
        "https://www.khinsider.com/"
    ];

    let random_index = Math.floor(Math.random() * random_sites.length);
    window.location.replace(random_sites[random_index]);
}

let seconds = 5;
let el = document.getElementById('seconds_counter');

function countDownSeconds() {
    if (seconds == 0) {
        randomSite();
        window.clearInterval(seconds);
    }

    el.innerText = "Redirecting to random site in " + seconds + " seconds.";
    seconds -= 1;
}

let temp = window.setInterval(countDownSeconds, 1000);