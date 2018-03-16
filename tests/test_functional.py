import pytest
import time
from django.urls import reverse


def test_page_api_integration(live_server, client, selenium, mocker):
    selenium.get(live_server.url)
    selenium.maximize_window()
    mocked_get_weather = mocker.patch('api.views.get_temperature_by_city')
    mocked_get_weather.return_value = {
        'temp' : 100,
        'pressure' : 40,
        'humidity' : 50,
        'temp_min' : 30,
        'temp_max' : 40,
    }
    cityText = selenium.find_element_by_id('inputCity')
    cityText.send_keys('Pistoia')
    startSearchButton = selenium.find_element_by_id('startSearch')
    startSearchButton.click()
    time.sleep(5)
    tempResultLabel = selenium.find_element_by_id('tempResults')
    assert tempResultLabel.text == 'In Pistoia there are 100°F'
    time.sleep(5)

