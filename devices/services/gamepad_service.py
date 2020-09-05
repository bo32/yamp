from pathlib import Path

import socket 

class GamepadService:
    def __init__(self):
        self.input_folder = Path('/dev/input')

    def get_input_folder_files(self):
        return sorted(self.input_folder.iterdir())

    def get_gamepads(self):
        result = []
        for file in self.get_input_folder_files():
            # print(file)
            if file.name.startswith('event'):
                result.append(str(file.absolute()))
        return result

    def attach_gamepad(self):
        print('Gamepads:')
        for file in self.get_gamepads():
            print('- ' + file)

            from multiprocessing import Process
            p = Process(target=self._start_listening_to_gamepad, args=(file,))
            p.start()
            # p.join()


    def _start_listening_to_gamepad(self, file):
        from evdev import InputDevice, ecodes, categorize
        gamepad = InputDevice(file)


        for event in gamepad.read_loop():
        #filters by event type
            if event.type == ecodes.EV_KEY:
                print(categorize(event))
                print(event)
                print(event.code)

                if event.code == 305 or event.code == '305' :
                    print("B")
                    import requests
                    requests.get('http://{}:8000/player/pause'.format(socket.gethostname()))

