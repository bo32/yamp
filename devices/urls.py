from django.urls import path

from devices import views


urlpatterns = [
    path('', views.show_devices, name='devices')
]
