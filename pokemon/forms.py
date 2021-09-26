from django import forms

from pokemon.models import pokedexVersion


class PokedexSelectForm(forms.Form):
    pokedex_choice = forms.ModelChoiceField(queryset=pokedexVersion.objects.exclude(pokemonversiondescription__version__isnull=True))

    def __init__(self, *args, **kwargs):
        super(PokedexSelectForm, self).__init__(*args, **kwargs)
        print(self.fields['pokedex_choice'].__dict__)
        print(dir(self.fields['pokedex_choice']))