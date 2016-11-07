from django.conf.urls import url
from .views import gmap_index

urlpatterns = [
    url(r'^$', gmap_index, name='index')
]
