import os
import json
import requests
from io import BytesIO
from places.models import Place, Image
from django.conf import settings
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Loads data from a JSON file into the database'

    @staticmethod
    def upload_images(place, urls):
        for num, url in enumerate(urls):
            response = requests.get(url)
            response.raise_for_status()
            image = BytesIO(response.content)
            image_name = os.path.basename(url)
            image_obj, created = place.images.get_or_create(
                place=place.id,
                order=num
            )
            image_obj.image.save(image_name, image, save=True)

    def handle(self, *args, **options):
        os.chdir(settings.LOAD_ROOT)
        for file in os.listdir("."):
            with open(file, 'r', encoding='utf-8') as file:
                serialized_json = json.load(file)

            place = Place.objects.create(
                title=serialized_json['title'],
                description_short=serialized_json['description_short'],
                description_long=serialized_json['description_long'],
                longitude=serialized_json['coordinates']['lng'],
                latitude=serialized_json['coordinates']['lat']
            )

            self.upload_images(place, serialized_json['imgs'])

            self.stdout.write(self.style.SUCCESS('Data loaded successfully'))
