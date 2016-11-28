from django import template
from django.conf import settings

register = template.Library()

@register.inclusion_tag('google-maps/map.html')
def googlemap(name, *args, **kwargs):

    """ Tag for rendering google maps """

    gmap = {}
    gmap['API_KEY'] = settings.GOOGLE_MAPS_API_KEY
    gmap['name'] = name

    try:
        gmap['markers'] = args[0]
    except IndexError:
        pass

    return gmap
