import os
import requests
from io import BytesIO
from places.models import Place
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Loads data from a JSON file into the database'

    def add_arguments(self, parser):
        parser.add_argument('json_url', type=str, help='The URL of the JSON file to load')

    @staticmethod
    def upload_images(place, urls):
        if not urls:
            return
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
        decoded_response = response.json()
        place, created = Place.objects.update_or_create(
            title=decoded_response['title'],
            defaults={
                'description_short': decoded_response.get('description_short', ''),
                'description_long': decoded_response.get('description_long', ''),
                'longitude': decoded_response['coordinates']['lng'],
                'latitude': decoded_response['coordinates']['lat']
            }
        )
        self.upload_images(place, decoded_response.get('imgs'))
        self.stdout.write(self.style.SUCCESS('Data loaded successfully'))
