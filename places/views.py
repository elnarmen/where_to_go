from django.shortcuts import render, get_object_or_404
from django.http.response import JsonResponse
from .models import Place
from django.urls import reverse


def get_place_details(place):
    place_details = {
        'title': place.title,
        'imgs': [image.image.url for image in place.images.all()],
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
            'lng': place.longitude,
            'lat': place.latitude
        }
    }

    return place_details


def show_map(request):

    places_query_set = Place.objects.all()

    places = {
      "type": "FeatureCollection",
      "features": []
    }

    for place in places_query_set:
        places["features"].append(
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [place.longitude, place.latitude]
                },
                "properties": {
                    "title": place.title,
                    "placeId": place.id,
                    "detailsUrl": reverse(
                        'show_place', kwargs={'place_id': place.pk}
                    )
                }
            }
        )

    places_geojson = {'places': places}

    return render(request, 'places/index.html', context=places_geojson)


def show_place(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    place_details = get_place_details(place)

    return JsonResponse(
        place_details,
        json_dumps_params={'ensure_ascii': False, 'indent': 4}
    )
