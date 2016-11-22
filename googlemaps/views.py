# -*- coding: utf-8 -*-
from django.shortcuts import render

def gmap_index(request):
    markers = [
    {
        "coords": {
            "lat": 53.13248859999999,
            "lng": 23.1688403
        },
        "name": "Bia\u0142ystok"
    },
    {
        "coords": {
            "lat": 53.12348040000001,
            "lng": 18.0084378
        },
        "name": "Bydgoszcz"
    },
    {
        "coords": {
            "lat": 54.35202520000001,
            "lng": 18.6466384
        },
        "name": "Gda\u0144sk"
    },
    {
        "coords": {
            "lat": 52.7325285,
            "lng": 15.2369305
        },
        "name": "Gorz\u00f3w Wielkopolski"
    },
    {
        "coords": {
            "lat": 50.26489189999999,
            "lng": 19.0237815
        },
        "name": "Katowice"
    },
    {
        "coords": {
            "lat": 50.8660773,
            "lng": 20.6285677
        },
        "name": "Kielce"
    },
    {
        "coords": {
            "lat": 50.06465009999999,
            "lng": 19.9449799
        },
        "name": "Krak\u00f3w"
    },
    {
        "coords": {
            "lat": 51.2464536,
            "lng": 22.5684463
        },
        "name": "Lublin"
    },
    {
        "coords": {
            "lat": 51.7592485,
            "lng": 19.4559833
        },
        "name": "\u0141\u00f3d\u017a"
    },
    {
        "coords": {
            "lat": 53.778422,
            "lng": 20.4801193
        },
        "name": "Olsztyn"
    },
    {
        "coords": {
            "lat": 50.6751067,
            "lng": 17.9212976
        },
        "name": "Opole"
    },
    {
        "coords": {
            "lat": 52.406374,
            "lng": 16.9251681
        },
        "name": "Pozna\u0144"
    },
    {
        "coords": {
            "lat": 50.0411867,
            "lng": 21.9991196
        },
        "name": "Rzesz\u00f3w"
    },
    {
        "coords": {
            "lat": 53.4285438,
            "lng": 14.5528116
        },
        "name": "Szczecin"
    },
    {
        "coords": {
            "lat": 53.0137902,
            "lng": 18.5984437
        },
        "name": "Toru\u0144"
    },
    {
        "coords": {
            "lat": 52.2296756,
            "lng": 21.0122287
        },
        "name": "Warszawa"
    },
    {
        "coords": {
            "lat": 51.1078852,
            "lng": 17.0385376
        },
        "name": "Wroc\u0142aw"
    },
    {
        "coords": {
            "lat": 51.9356214,
            "lng": 15.5061862
        },
        "name": "Zielona G\u00f3ra"
    }
]
    return render(request, 'google-maps/index.html', {'markers': markers})
