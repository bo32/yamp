_MUTE = 'mute'

function pause() {
    send('pause');
}

function previous() {
    send('previous');
}

function next() {
    send('next');
}

function mute() {
    send(_MUTE);
}

function play(folder) {
    send('play/' + folder);
}

function send(action) {
    const http = new XMLHttpRequest();
    http.onreadystatechange = function() {
        if (http.readyState == XMLHttpRequest.DONE) {
            if (action === _MUTE) {
                const json_response = JSON.parse(http.responseText);
                document.getElementById("mute_button").innerHTML = json_response.muted ? "Unmute" : "Mute";
            }
        }
    }
    http.open("GET", action);
    http.send();
}