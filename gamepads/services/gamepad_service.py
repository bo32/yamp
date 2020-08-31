import os

class GamepadService:

    def __init__(self):
        pass

    def get_devices(self):
#         files = (str(file) for file in sorted(self.device_folder.iterdir()))
#         for file in files:
#             print(file)
#         return files
#         os.system('bluetoothctl paired-devices')
        stream = os.popen('bluetoothctl paired-devices')
        output = stream.read()
        print(output)
        return ('empty')