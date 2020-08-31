from django.urls import path

from gamepads import views


urlpatterns = [
    path('', views.show_gamepads, name='gamepads')
]
