from django.core.management.base import BaseCommand

from pokemon.utils import obtain_pokemon
    
class Command(BaseCommand):
    help = 'obtain pokemon'

    def handle(self, *args, **options):
        obtain_pokemon()
