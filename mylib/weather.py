import requests


class WeatherAPIError(Exception):
    pass


class WeatherConnectionError(Exception):
    pass


def get_temperature_by_city(city):
    app_id = '8440aa26c4c91dc0c70e5a348d603b9a'
    weather_url = 'http://api.openweathermap.org/data/2.5/weather?q={0}&APPID={1}'.format(
        city, app_id
    )
    try:
        resp = requests.get(weather_url)
        if resp.status_code != 200:
            raise WeatherAPIError('Error using API!')
    except requests.exceptions.ConnectionError as ex:
        raise WeatherConnectionError('Connection error!')
    return resp.json()['main']