Django Google Maps
=======================

**Django Google Maps** - django app for displaying Google Maps.

Meta
----

Author:
    Radosław "Duch" Przytuła

Django version:
    1.10

Version:
    1.0

Usage
-----
- Include `google-maps` in your INSTALLED_APPS in settings file.

- Add your Google Maps API Key in your settings file as `GOOGLE_MAPS_API_KEY`

- Include {% google_map 'map_name' %} into your template where 'map_name' is maps name.

- Optionally you can pass list of markers as template tags argument. List should be in such format:

In view.py:

  markers = [ 
    {'name': 'marker_name_1', 'lng': 50.3054, 'lat': 20.3049 },
    {'name': 'marker_name_2', 'lng': 51.3040, 'lat': 21.3984 }
  ]

In template:

  {% google_map 'map_name' markers %}
