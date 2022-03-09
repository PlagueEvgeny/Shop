import json

from django.core.management.base import BaseCommand
from authapp.models import Profile


class Command(BaseCommand):
    help = 'Makes reserve copy'

    def handle(self, *args, **options):
        with open('dump/profile.json', 'r', encoding='utf-8') as f:
            data_for_resore = json.load(f)

        for item in data_for_resore:
            Profile.objects.create(**{
                'login': item['login'],
                'password': item['password'],
            })
