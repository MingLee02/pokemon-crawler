from django.db import models


class pokemon(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True,
    )
    pokedex_id = models.PositiveIntegerField()
    sprite = models.ImageField(upload_to="sprite/",)
    height = models.CharField(max_length=255)
    weight = models.CharField(max_length=255)
    type_one = models.CharField(max_length=255)
    type_two = models.CharField(max_length=255)
    health_points = models.CharField(max_length=255)
    attack = models.CharField(max_length=255)
    defence = models.CharField(max_length=255) 
    speed = models.CharField(max_length=255)

    def __str__(self):
        return self.name
        
class pokedexVersion(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True,
    )
    
    def __str__(self):
        return self.name


class pokemonVersionDescription(models.Model):
    pokemon = models.ForeignKey(pokemon, on_delete=models.CASCADE)
    version = models.ForeignKey(pokedexVersion, on_delete=models.CASCADE)

