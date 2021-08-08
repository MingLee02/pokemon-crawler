from django.test import TestCase

from requests import HTTPError

from pokemon.management.commands.get_pokedex_version import checkUrl


class VersionTest(TestCase):
    def test_checkUrl_fail(self, requests_mock):
        requests_mock.get(f'pokemon_url_somthing', status_code=404)
        response = checkUrl('pokemon_url_somthing')
        assert response == 'Error'
