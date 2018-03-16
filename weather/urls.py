from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.weather_index, name='weather-index'),
]