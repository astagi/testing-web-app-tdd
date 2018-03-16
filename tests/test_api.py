import json
import pytest
from django.urls import reverse
from mylib.weather import WeatherAPIError


def test_api(client, mocker):
    mocked_get_weather = mocker.patch('api.views.get_temperature_by_city')
    mocked_get_weather.return_value = {
        'temp' : 100,
        'pressure' : 40,
        'humidity' : 50,
        'temp_min' : 30,
        'temp_max' : 40,
    }
    response = client.get('/api/temperature?city=Pistoia')
    assert response.status_code == 200
    json_response = json.loads(response.content.decode())
    assert json_response['temp'] == 100
    assert json_response['pressure'] == 40
    assert json_response['humidity'] == 50
    assert json_response['temp_min'] == 30
    assert json_response['temp_max'] == 40


def test_api_on_error(client, mocker):
    mocked_get_weather = mocker.patch('api.views.get_temperature_by_city')
    mocked_get_weather.side_effect = WeatherAPIError
    response = client.get('/api/temperature?city=')
    assert response.status_code == 500
