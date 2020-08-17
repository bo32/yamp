# from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def show_player(request):
    from player.services.player_service import PlayerService
    player_service = PlayerService()

    current_track = player_service.get_current_track()

    print(current_track)
    return render(request, 'player.html', current_track)