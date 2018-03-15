from mylib.weather import get_temperature_by_city


def test_get_temperature_by_city():
    temperature = get_temperature_by_city('Pistoia')
    assert temperature['temp'] == '279.61'
    assert temperature['pressure'] == '1071'
    assert temperature['humidity'] == '100'
    assert temperature['temp_min'] == '272.31'
    assert temperature['temp_max'] == '282.31'