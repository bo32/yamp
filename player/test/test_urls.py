from django.test import SimpleTestCase
from django.urls import reverse, resolve

from player.rest import sound_up
from player.views import show_player

class TestUrls(SimpleTestCase):

    def test_play(self):
        self.check_url('player', show_player)

    def test_sound_up(self):
        self.check_url('sound_up', sound_up)

    def test_sound_down(self):
        self.check_url('sound_down', sound_down)

    def check_url(self, url_str, func):
        url = reverse(url_str)
        print(resolve(url))
        self.assertEquals(resolve(url).func, func)
