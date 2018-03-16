from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^temperature$', views.get_temperature_from_city, name='api-temperature'),
]