from django.http import HttpResponse

from player.services.player_service import PlayerService
from player.services.url_service import UrlService

from django.views.decorators.http import require_http_methods



player_service = PlayerService()
url_service = UrlService()

@require_http_methods(["GET"])
def play(request, album):
    player_service.play(album)
    return HttpResponse('PLAYING')

@require_http_methods(["GET"])
def next(request):
    player_service.next()
    print('next')
    return HttpResponse('NEXT')

@require_http_methods(["GET"])
def previous(request):
    player_service.previous()
    return HttpResponse('PREVIOUS')

@require_http_methods(["GET"])
def pause(request):
    player_service.pause()
    return HttpResponse('PAUSED')

@require_http_methods(["GET"])
def sound_up(request):
    player_service.sound_up()
    return HttpResponse('SOUND_UP')

@require_http_methods(["GET"])
def sound_down(request):
    player_service.sound_down()
    return HttpResponse('SOUND_DOWN')

@require_http_methods(["GET"])
def toggle_mute(request):
    #TODO player_service.toggle_mute()
    return HttpResponse('TOGGLE MUTE')

# Audio stream
@require_http_methods(["GET"])
def play_url(request, url_key):
    url = url_service.get_url(url_key)
    print('Retrieved URL: ' + url)
    # Handled if there are no found URLs
    player_service.play_url(url)
    return HttpResponse('PLAYING ' + url)
