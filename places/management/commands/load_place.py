import os
import json
import requests
from io import BytesIO
from places.models import Place, Image
from django.conf import settings
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Loads data from a JSON file into the database'

    def add_arguments(self, parser):
        parser.add_argument('json_url', type=str, help='The URL of the JSON file to load')

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
        json_url = options['json_url']
        response = requests.get(json_url)
        response.raise_for_status()
        decoded_json = response.json()
        place = Place.objects.create(
            title=decoded_json['title'],
            description_short=decoded_json['description_short'],
            description_long=decoded_json['description_long'],
            longitude=decoded_json['coordinates']['lng'],
            latitude=decoded_json['coordinates']['lat']
        )

        self.upload_images(place, decoded_json['imgs'])

        self.stdout.write(self.style.SUCCESS('Data loaded successfully'))
