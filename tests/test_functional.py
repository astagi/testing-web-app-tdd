import pytest
import time
from django.urls import reverse


def test_page_api_integration(live_server, client, selenium):
    print (client.__dict__)
    selenium.get(live_server.url)
    selenium.maximize_window()
    cityText = selenium.find_element_by_id('inputCity')
    cityText.send_keys('Pistoia')
    startSearchButton = selenium.find_element_by_id('startSearch')
    startSearchButton.click()
    time.sleep(5)
    tempResultLabel = selenium.find_element_by_id('tempResults')
    time.sleep(5)

