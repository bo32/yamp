from django.shortcuts import render

from gamepads.services.gamepad_service import GamepadService

def show_gamepads(request):
    gs = GamepadService()
    devices = gs.get_devices()

    content = {
        'devices': devices
    }

    return render(request, 'gamepads.html', content)



