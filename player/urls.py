from django.urls import path

from player import rest
from player import views


urlpatterns = [
    path('', views.show_player, name='player'),
    path('play/<album>', rest.play),
    path('pause/', rest.pause),
    path('next/', rest.next),
    path('previous/', rest.previous),
    path('sound_up/', rest.sound_up, name='sound_up'),
    path('sound_down/', rest.sound_down, name='sound_down'),
    path('mute/', rest.mute),
#     path('shutdown/', rest.toggle_mute),
    path('play_url/<url_key>', rest.play_url)
]
