from mylib.weather import get_temperature_by_city


def test_get_temperature_by_city(mocker):

    mock_weather_response = {
        "coord":{
            "lon":10.92,
            "lat":43.93
        },
        "weather":[
            {
                "id":501,
                "main":"Rain",
                "description":"moderate rain",
                "icon":"10d"
            },
            {
                "id":600,
                "main":"Snow",
                "description":"light snow",
                "icon":"13d"
            },
            {
                "id":741,
                "main":"Fog",
                "description":"fog",
                "icon":"50d"
            }
        ],
        "base":"stations",
        "main":{
            "temp":279.61,
            "pressure":1071,
            "humidity":100,
            "temp_min":272.31,
            "temp_max":282.31
        },
        "visibility":8000,
        "wind":{
            "speed":4.6,
            "deg":100
        },
        "clouds":{
            "all":90
        },
        "dt":1521132900,
        "sys":{
            "type":1,
            "id":5861,
            "message":0.0041,
            "country":"IT",
            "sunrise":1521091659,
            "sunset":1521134588
        },
        "id":6541867,
        "name":"Pistoia",
        "cod":200
    }

    mocked_requests_get = mocker.patch('mylib.weather.requests.get')
    mocked_requests_get.return_value.status_code = 200
    mocked_requests_get.return_value.json.return_value = mock_weather_response
    temperature = get_temperature_by_city('Pistoia')
    assert temperature['temp'] == 279.61
    assert temperature['pressure'] == 1071
    assert temperature['humidity'] == 100
    assert temperature['temp_min'] == 272.31
    assert temperature['temp_max'] == 282.31