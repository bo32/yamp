from django.urls import path

from player import rest
from player import views


urlpatterns = [
    path('', views.show_player, name='player'),
    path('play/<album>', rest.play),
    path('pause/', rest.pause),
    path('next/', rest.next),
    path('previous/', rest.previous),
    path('soundup/', rest.sound_up, name='soundup'),
    path('sounddown/', rest.sound_down),
    path('mute/', rest.mute),
#     path('shutdown/', rest.toggle_mute),
    path('play_url/<url_key>', rest.play_url)
]
