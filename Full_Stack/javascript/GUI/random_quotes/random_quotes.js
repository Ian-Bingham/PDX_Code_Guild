// get quote of the day
function qotd() {
    fetch('https://favqs.com/api/qotd')
        .then(function (response) {
            return response.json();
        })
        .catch((error) => console.log(error))
        .then(function (myJson) {
            let quote = myJson['quote']['body'];
            let author = myJson['quote']['author'];
            $('#qotd .quote').text(`"${quote}"`);
            $('#qotd .author').text(`- ${author}`);
        });
}

function fetchQuotes(url) {
    let header = new Headers();
    header.append('Authorization', 'Token token="{INSERT API KEY HERE}"');
    fetch(`${url}`, {
        method: 'GET',
        headers: header
    }).then((response) => response.json())
        .catch((error) => console.log(error))
        .then((myJSON) => {
            let quoteList = myJSON.quotes;
            for (let i = 0; i < quoteList.length; i++) {
                let quote = quoteList[i].body;
                let author = quoteList[i].author;
                $('#quoteList').append(`<li id="quote${i}">\
                                            <h2 class="quote">"${quote}"</h2>\
                                            <h3 class="author">- ${author}</h3>\
                                        </li>`)
            }
        });
}

// allow searching for quotes
function getSearchQuote() {
    let url = 'https://favqs.com/api/quotes';
    let searchInput = $('#searchInput').val();
    let searchFilter = $('#filter').val();
    if (searchInput != '') {
        switch (searchFilter) {
            case 'keyword':
                url += `/?filter=${searchInput}`;
                break;
            case 'tag':
                url += `/?filter=${searchInput}&type=tag`;
                break;
            case 'author':
                searchInput.replace(' ', '+');
                url += `/?filter=${searchInput}&type=author`;
                break;
        }
    }
    return url;
}

$('#submit').on('click', function () {
    $('#quoteList').empty();
    fetchQuotes(getSearchQuote());
});

qotd();
