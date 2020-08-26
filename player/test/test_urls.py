from django.test import SimpleTestCase
from django.urls import reverse, resolve

from player.rest import sound_up
from player.views import show_player

class TestUrls(SimpleTestCase):

    def test_play(self):
        self.check_url('player', show_player)

    def test_soundup(self):
        self.check_url('soundup', sound_up)

    def check_url(self, url_str, func):
        url = reverse(url_str)
        print(resolve(url))
        self.assertEquals(resolve(url).func, func)
