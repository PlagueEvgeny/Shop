import json

from django.core.management.base import BaseCommand
from authapp.models import Profile


class Command(BaseCommand):
    help = 'Makes reserve copy'

    def handle(self, *args, **options):
        items = Profile.objects.all()
        data_for_dump = []
        for item in items:
            data_for_dump.append({
                'login': item.login,
                'password': item.password,
            })
        with open('dump/profile.json', 'w', encoding='utf-8') as f:
            json.dump(data_for_dump, f)