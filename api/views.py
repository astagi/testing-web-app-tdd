from django.http import JsonResponse
from django.shortcuts import render

from mylib.weather import get_temperature_by_city, WeatherAPIError


def get_temperature_from_city(request):
    try:
        temperature = get_temperature_by_city(request.GET.get('city', ''))
        return JsonResponse(temperature)
    except WeatherAPIError as ex:
        return JsonResponse(
            {'details' : 'Something \'s wrong, please try again!'},
            status=500
        )