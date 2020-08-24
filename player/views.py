# from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def show_player(request):
    from player.services.player_service import PlayerService
    player_service = PlayerService()

    # get currently playing track
    current_track = player_service.get_current_track()

    # get music library folder
    from player.global_properties import global_properties
    from pathlib import Path
    library_folder = Path(global_properties['DEFAULT']['library_path'])
    folder = [x.name for x in library_folder.iterdir() if x.is_dir()]

    content = {
        'current_track': current_track,
        'folder': folder
    }

    return render(request, 'player.html', content)