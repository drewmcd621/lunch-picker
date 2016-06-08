from django.core.management.base import BaseCommand, CommandError
from picker.services import get_choices

class Command(BaseCommand):

        def handle(self, *args, **options):
            get_choices()
