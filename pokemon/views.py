import re

from django.views.generic import DetailView, ListView
from django.views.generic.edit import FormView
from django.urls import reverse

from pokemon.models import pokemon, pokemonVersionDescription, pokedexVersion
from pokemon.forms import PokedexSelectForm


class HomeView(FormView):
    template_name = 'home.html'
    form_class = PokedexSelectForm

    def get_success_url(self):
        return reverse(
            'pokemon-list',
            kwargs={'version_id': self.request._post.get('pokedex_choice')}
        )


class PokemonListView(ListView):
    template_name = "pokemon_list.html"
    model = pokemon
    context_object_name = 'pokemon'

    def get_queryset(self):
        version = pokedexVersion.objects.get(id=self.kwargs.get('version_id'))
        queryset = pokemon.objects.filter(pokemonversiondescription__version__name=version.name).order_by('id')
     
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dex_version'] = pokedexVersion.objects.get(id=self.kwargs.get('version_id')).name
        return context


class PokemonDetailView(DetailView):
    template_name = "pokemon.html"
    model = pokemon

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        selected_pokemon = self.object.pokemonversiondescription_set.filter(version__name='blue').first()

        context['pokedex_version'] = selected_pokemon.version.id
        context['pokemon_desc'] = re.sub(r'[^\w.]', ' ', selected_pokemon.description)
        
        return context

