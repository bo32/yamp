from pathlib import Path

properties_folder_path = Path.home().joinpath('.yamp')
if not properties_folder_path.exists():
    print('creating {} folder...'.format(str(properties_folder_path)))
    properties_folder_path.mkdir()

properties_file_path = properties_folder_path.joinpath('application.ini')
if not properties_file_path.exists():
    properties_file_path.touch()
    with open(str(properties_file_path), 'w') as file:
        file.write('[DEFAULT]\n')
        file.write('library_path=~/Music\n')

# TODO add a listener on the config files and restart/update app ?
import configparser
global_properties = configparser.ConfigParser()
global_properties.read(str(properties_file_path))

print('Global properties:')
for key in global_properties['DEFAULT']:
    print(' - {}: {}'.format(key, global_properties['DEFAULT'][key]))