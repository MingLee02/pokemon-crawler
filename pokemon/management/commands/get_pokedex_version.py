import requests
import json

from django.core.management.base import BaseCommand
from django.http import HttpResponseNotFound

from pokemon.models import pokedexVersion
from .command_utils import checkUrl


def create_version(versions):
    for version in versions:
        pokedexVersion.objects.update_or_create(
            name=version['name']
        )


def obtain_pokedex_versions(records):
    for record in records:
        response = checkUrl(record['url'])
        if response == 'Error':
            pass
    
        versions = json.loads(response.text).get('versions', None)
        if versions:
            create_version(versions)


class Command(BaseCommand):
    help = 'obtain pokedex versions'

    def handle(self, *args, **options):
        base_url = "https://pokeapi.co/api/v2/version-group/"
        response = checkUrl(base_url)

        if response == 'Error':
            return HttpResponseNotFound()
        
        records = json.loads(response.text).get('results', None)

        if records:
            obtain_pokedex_versions(records)

