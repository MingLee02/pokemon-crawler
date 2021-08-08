from requests import HTTPError

from pokemon.management.commands.get_pokedex_version import checkUrl


def test_checkUrl_fail(requests_mock):
    requests_mock.get('pokemon_url_somthing', status_code=404)
    response = checkUrl('pokemon_url_somthing')
    assert response == 'Error'
