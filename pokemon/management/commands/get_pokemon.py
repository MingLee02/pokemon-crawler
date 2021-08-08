import requests
import json

from django.core.management.base import BaseCommand
from django.http import HttpResponseNotFound

from pokemon.models import pokedexVersion, pokemon
from .command_utils import checkUrl



def obtain_pokemon(version='blue', start='scratch', limit=10):
    version = pokedexVersion.objects.filter(name=version)

    if version:
        if start == 'scratch':
            for count in range(1, limit):
                url = "https://pokeapi.co/api/v2/pokemon/{}".format(count)
                response = checkUrl(url)
                if response == 'Error':
                    pass
                print(  json.loads(response.text))
                data = json.loads(response.text).get('versions', None)
                1/0
    else:
        return 'No matching version'

    
class Command(BaseCommand):
    help = 'obtain pokemon'

    def handle(self, *args, **options):
        base_url = "https://pokeapi.co/api/v2/pokemon/"
        obtain_pokemon()
