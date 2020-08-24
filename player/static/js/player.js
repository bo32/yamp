function pause() {
    send('pause');
}

function previous() {
    send('previous');
}

function next() {
    send('next');
}

function play(folder) {
    send('play/' + folder);
}

function send(action) {
    const http = new XMLHttpRequest();
    http.open("GET", action);
    http.send();
}