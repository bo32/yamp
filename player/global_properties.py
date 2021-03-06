from pathlib import Path

properties_folder_path = Path.home().joinpath('.yamp')
if not properties_folder_path.exists():
    print('creating {} folder...'.format(str(properties_folder_path)))
    properties_folder_path.mkdir()

properties_file_path = properties_folder_path.joinpath('application.ini')
if not properties_file_path.exists():
    properties_file_path.touch()
    with open(str(properties_file_path), 'w') as file:
        # [server]
        file.write('[server]\n')
        # library_path
        default_music_folder=Path.home().joinpath('Music')
        file.write('library_path={}\n'.format(str(default_music_folder)))
        # enable_nfc_scanning
        file.write('enable_nfc_scanning=no\n')
        # enable_gamepads
        file.write('enable_gamepads=no\n')
        file.write('\n')

        # [urls]
        file.write('[urls]\n')
        file.write('# Add your URLs below (eg. franceinter=http://direct.franceinter.fr/live/franceinter-midfi.mp3\n')
    
else:
    pass # TODO check if all sections are present

# TODO add a listener on the config files and restart/update app ?
import configparser
global_properties = configparser.ConfigParser()
global_properties.read(str(properties_file_path))

print('Loaded properties:')
for section in global_properties.sections():
    print('[{}]'.format(section))
    for key in global_properties[section]:
        print(' - {}: {}'.format(key, global_properties[section][key]))

def get_boolean_property_value(section, key):
    return global_properties[section].getboolean(key)