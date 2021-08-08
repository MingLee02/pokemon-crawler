from io import StringIO

from django.core.management import call_command
from django.test import TestCase

from pokemon.models import pokedexVersion


class GetVersionsTestCase(TestCase):
    def call_command(self, *args, **kwargs):
        out = StringIO()
        call_command(
            "get_pokedex_version",
            *args,
            stdout=out,
            stderr=StringIO(),
            **kwargs,
        )
        return out.getvalue()
    
    def test_write(self):
        assert pokedexVersion.objects.filter(name='blue').count() == 0
        out = self.call_command()

        assert pokedexVersion.objects.filter(name='blue').count() == 1
