from django.http import HttpResponse, JsonResponse

from player.services.player_service import PlayerService
from player.services.url_service import UrlService

from django.views.decorators.http import require_http_methods

@require_http_methods(["GET"])
def play(request, album):
    PlayerService().play(album)
    current_track = PlayerService().get_current_track()
#     return HttpResponse('PLAYING')
    return JsonResponse(current_track)


def play_index(request, index):
    PlayerService().play_index(index)
    current_track = PlayerService().get_current_track()
    return JsonResponse(current_track)

@require_http_methods(["GET"])
def next(request):
    PlayerService().next()
    current_track = PlayerService().get_current_track()
    return JsonResponse(current_track)

@require_http_methods(["GET"])
def previous(request):
    PlayerService().previous()
    current_track = PlayerService().get_current_track()
    return JsonResponse(current_track)

@require_http_methods(["GET"])
def pause(request):
    PlayerService().pause()
    return HttpResponse('PAUSED')

@require_http_methods(["GET"])
def sound_up(request):
    data = PlayerService().sound_up()
    return JsonResponse(data)

@require_http_methods(["GET"])
def sound_down(request):
    data = PlayerService().sound_down()
    return JsonResponse(data)

@require_http_methods(["GET"])
def mute(request):
    muted = PlayerService().toggle_mute()
    response_data = {'muted': muted}
    return JsonResponse(response_data)

# Audio stream
@require_http_methods(["GET"])
def play_url(request, url_key):
    url = UrlService().get_url(url_key)
    print('Retrieved URL: ' + url)
    # Handled if there are no found URLs
    PlayerService().play_url(url)
    return HttpResponse('PLAYING ' + url)
