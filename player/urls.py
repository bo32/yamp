from django.urls import path

from player import rest
from player import views


urlpatterns = [
    path('', views.show_player),
    path('play/<album>', rest.play),
    path('pause/', rest.pause),
    path('next/', rest.next),
    path('previous/', rest.previous),
    path('soundup/', rest.sound_up),
    path('sounddown/', rest.sound_down)
]