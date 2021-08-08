from django.contrib import admin

from pokemon import models

admin.site.register(models.pokemon)
admin.site.register(models.pokedexVersion)
admin.site.register(models.pokemonVersionDescription)
