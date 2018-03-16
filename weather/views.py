from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

def weather_index(request):
    return render(request, 'weather/index.html')