function pause() {
    send('pause');
}

function previous() {
    send('previous');
}

function next() {
    send('next');
}

function send(action) {
    const http = new XMLHttpRequest();
    http.open("GET", action);
    http.send();
}