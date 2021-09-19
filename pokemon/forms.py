from django import forms

from pokemon.models import pokedexVersion


class PokedexSelectForm(forms.Form):
    pokedex_choice = forms.ModelChoiceField(queryset=pokedexVersion.objects.exclude(pokemonversiondescription__version__isnull=True))
