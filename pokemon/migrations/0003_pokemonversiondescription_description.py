# Generated by Django 3.2.6 on 2021-08-08 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0002_alter_pokemon_sprite'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemonversiondescription',
            name='description',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]