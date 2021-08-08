from django.views.generic import DetailView, ListView

from pokemon.models import pokemon, pokemonVersionDescription


class PokemonListView(ListView):
    template_name = "pokemon_list.html"
    model = pokemon
    context_object_name = 'pokemon'

    def get_queryset(self):
        queryset = pokemon.objects.filter(pokemonversiondescription__version__name='blue')
     
        return queryset


class PokemonDetailView(DetailView):
    template_name = "pokemon.html"
    model = pokemon

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['pokemon_desc'] = self.object.pokemonversiondescription_set.filter(version__name='blue').first().description

        return context

