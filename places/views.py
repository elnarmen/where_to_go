from django.shortcuts import render
from .models import Place


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
                    "placeId": place.pk,
                    "detailsUrl": "/static/places/moscow_legends.json"
                }
            }
        )

    places_geojson = {'places': places}

    return render(request, 'index.html', context=places_geojson)


