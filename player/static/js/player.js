_MUTE = 'mute'
_SOUND_UP = 'sound_up'
_SOUND_DOWN = 'sound_down'

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

function sound_down() {
    send(_SOUND_DOWN);
}

function sound_up() {
    send(_SOUND_UP);
}

function play(folder) {
    send('play/' + folder);
}

function send(action) {
    const http = new XMLHttpRequest();
    http.onreadystatechange = function() {
        if (http.readyState == XMLHttpRequest.DONE) {
            const json_response = JSON.parse(http.responseText);
            switch(action) {
                case _MUTE:
                    document.getElementById("mute_button").innerHTML = json_response.muted ? "Unmute" : "Mute";
                    break;
                case _SOUND_DOWN:
                case _SOUND_UP:
                    console.log(json_response.is_sound_max);
                    console.log(json_response.is_sound_min);
                    document.getElementById("sound_down").disabled = json_response.is_sound_min;
                    document.getElementById("sound_up").disabled = json_response.is_sound_max;
                    break;
                default:
                    break;
            }
        }
    }
    http.open("GET", action);
    http.send();
}