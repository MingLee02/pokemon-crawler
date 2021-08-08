from io import StringIO

from django.core.management import call_command
from django.test import TestCase

from pokemon.utils import obtain_pokemon
from pokemon.models import pokedexVersion, pokemon, pokemonVersionDescription


class GetPokemonTestCase(TestCase):
    def test_add_one_pokemon_yellow(self):
        pokedexVersion.objects.create(name='yellow')
        assert pokemonVersionDescription.objects.filter(version__name='yellow').count() == 0
        obtain_pokemon(version='yellow', limit=2)
        assert pokemonVersionDescription.objects.filter(version__name='yellow').count() == 1
    
    def test_add_ten_pokemon_yellow_skipping_first_one(self):
        pokedexVersion.objects.create(name='yellow')
    
        obtain_pokemon(version='yellow', limit=2)
        
        pokemon_count = pokemon.objects.all().count()

        assert pokemon_count == 1

        response, pokemon_list = obtain_pokemon(version='yellow', start="continue", limit=11)
        
        pokemon_count = pokemon.objects.all().count() 

        assert response.name == 'bulbasaur'
        assert 'bulbasaur' not in pokemon_list
        assert pokemon_count == 10