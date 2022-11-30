import csv

from datetime import date

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            id = int(phone['id'])
            name = phone['name']
            image = phone['image']
            price = int(phone['price'])
            release_date = date.fromisoformat(phone['release_date'])
            lte_exists = True if phone['lte_exists'] == 'True' else False
            slug = name.lower().replace(' ', '-')
            Phone.objects.create(id=id, name=name, image=image, price=price,
                                 release_date=release_date, lte_exists=lte_exists,
                                 slug=slug)
