import requests

def get_temperature_by_city(city):
    app_id = '8440aa26c4c91dc0c70e5a348d603b9a'
    weather_url = 'http://api.openweathermap.org/data/2.5/weather?q={0}&APPID={1}'.format(
        city, app_id
    )
    resp = requests.get(weather_url)
    return resp.json()['main']