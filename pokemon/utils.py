import requests
import json

from django.core.files.base import ContentFile

from pokemon.models import pokedexVersion, pokemon, pokemonVersionDescription
from pokemon.management.commands.command_utils import checkUrl


def create_pokemon_entry(record):
    pokemon_obj , _ = pokemon.objects.get_or_create(
        pokedex_id=record.get('id'),
        name=record.get('name'),
        weight=record.get('weight'),
        height = record.get('height')
    )
    pokemon_types = record.get('types')

    image_response = checkUrl(record.get('sprites').get('front_default'))

    data =  ContentFile(image_response.content)
    stats = record.get('stats')

    pokemon_obj.type_one = pokemon_types[0]['type']['name']
    if len(pokemon_types) == 2:
        pokemon_obj.type_two = pokemon_types[1].get('type').get('name', None)
    pokemon_obj.sprite.save(record.get('name'), data)
    pokemon_obj.health_points = stats[0]['base_stat']
    pokemon_obj.attack = stats[1]['base_stat']
    pokemon_obj.defence = stats[2]['base_stat']
    pokemon_obj.speed = stats[5]['base_stat']
    pokemon_obj.save()

    return pokemon_obj


def obtain_pokemon(version='yellow', start='scratch', limit=10):
    version = pokedexVersion.objects.filter(name=version)
    skipped = False
    pokemon_scraped = []
    if version:
        if start == 'scratch':
            start_num = 1
        else:
            start_num = pokemon.objects.all().count() + 1
            skipped = pokemon.objects.last()
            
        for count in range(start_num, limit):
            url = "https://pokeapi.co/api/v2/pokemon/{}".format(count)
            response = checkUrl(url)
            if response == 'Error':
                pass

            records = json.loads(response.text)
            if records:
                pokemon_obj = create_pokemon_entry(records)

                species_url = 'https://pokeapi.co/api/v2/pokemon-species/{}'.format(pokemon_obj.name)
                response = checkUrl(species_url)
                if response == 'Error':
                    pass

                species_info = json.loads(response.text)
                text_entries = species_info.get('flavor_text_entries')
                text_entry = [info for info in text_entries if info['version']['name'] == version[0].name]
                if text_entry:
                    pokemon_desc, _ = pokemonVersionDescription.objects.get_or_create(
                        pokemon=pokemon_obj,
                        version=version[0],
                    )
                    pokemon_desc.description = text_entry[0].get('flavor_text')
                    pokemon_desc.save()
                
                pokemon_scraped.append(pokemon_obj.name)
        if skipped:
            return skipped, pokemon_scraped
    else:
        return 'No matching version'
