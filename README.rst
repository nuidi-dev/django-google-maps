Django Google Maps
=======================

**Django Google Maps** - django app for displaying Google Maps.

Meta
----

Author:
    Radosław Przytuła

Django version:
    1.10

Version:
    1.0

Usage
-----
- Include `googlemaps` in your INSTALLED_APPS in settings file.

- Add your Google Maps API Key in your settings file as `GOOGLE_MAPS_API_KEY`

- Include {% googlemap 'map_name' %} into your template where 'map_name' is your maps name.

- Optionally you can pass list of markers as template tags argument. List should be in format:

  markers = [
    {'name': 'marker_name_1', 'lng': 50.3054, 'lat': 20.3049 },
    {'name': 'marker_name_2', 'lng': 51.3040, 'lat': 21.3984 }
  ]
