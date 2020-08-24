import vlc
import os

VOLUME_STEP = 5
VOLUME_MAX = 100
VOLUME_MIN = 0

META_DICTIONARY = {
    'title': 0,
    'artist_name': 1,
    'genre': 2,
    'album': 4,
    'date': 8
}

class PlayerService(object):

    _instance = None

    # https://python-patterns.guide/gang-of-four/singleton/#a-more-pythonic-implementation
    def __new__(cls):
        if cls._instance is None:
            print('Initializing Player Service...')
            cls._instance = super(PlayerService, cls).__new__(cls)
            # FIXME I guess some errors are triggered from here is VLC is not installed on the machine. Errors to be caught
            cls._instance.instance = vlc.Instance('--loop')
            cls._instance.list_player = cls._instance.instance.media_list_player_new()
            cls._instance.played_album = None
            print('Player Service initialized...')
        return cls._instance

    def get_media_player(self):
        return self.list_player.get_media_player()

    def get_current_track(self):
        if self.played_album is None:
            return {'title': 'nothing'}

        current_track = self.get_media_player().get_media()
        current_track.parse()
        result = {}
        for key in META_DICTIONARY.keys():
            result[key] = current_track.get_meta(META_DICTIONARY[key])
        return result

    def change_sound(self, direction):
        current_volume = self.get_current_volume()
        if direction == 'up':
            new_volume = VOLUME_MAX if current_volume > VOLUME_MAX - VOLUME_STEP else current_volume + VOLUME_STEP
        elif direction == 'down':
            new_volume = VOLUME_MIN if current_volume < VOLUME_STEP else current_volume - VOLUME_STEP
        else:
            raise Exception('wrong volume direction')
        print('setting sound to ' + str(new_volume))
        self.get_media_player().audio_set_volume(new_volume)

    def sound_up(self):
        print('sound up')
        self.change_sound('up')

    def sound_down(self):
        print('sound down')
        self.change_sound('down')

    def get_current_volume(self):
        return self.get_media_player().audio_get_volume()

    def pause(self):
        self.list_player.pause()

    def next(self):
        self.list_player.next()

    def previous(self):
        self.list_player.previous()

    def play(self, directory):
        from player.global_properties import global_properties
        from pathlib import Path
        library_folder = Path(global_properties['DEFAULT']['library_path'])
        dir_to_play = library_folder.joinpath(directory)
        dir_to_play = str(dir_to_play)
        print('playing album ' + dir_to_play)

        self.played_album = self.instance.media_list_new()
        # TODO filter only sound files
        for song in os.listdir(dir_to_play):
            print('Adding ' + os.path.join(dir_to_play, song))
            media = self.instance.media_new(os.path.join(dir_to_play, song))
            self.played_album.add_media(media)

        self.list_player.stop()
        self.list_player.set_media_list(self.played_album)
        self.list_player.play()
        print('Playing music...')
