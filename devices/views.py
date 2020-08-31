from django.shortcuts import render

from devices.services.device_service import DeviceService

def show_devices(request):
    gs = DeviceService()
    devices = gs.get_devices()
    paired_devices = gs.get_paired_devices()

    content = {
        'devices': devices,
        'paired_devices': paired_devices
    }

    return render(request, 'devices.html', content)
