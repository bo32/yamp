import os

class DeviceService:

    def __init__(self):
        pass

    def _get_command_output(self, command):
        stream = os.popen(command)
        return stream.read().split('\n')[:-1] # last element is empty string

    def get_paired_devices(self):
        return self._get_command_output('sudo bluetoothctl paired-devices')

    def get_devices(self):
        return self._get_command_output('sudo bluetoothctl devices')
    