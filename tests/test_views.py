import pytest
from django.urls import reverse


def test_main_view(client):
    url = reverse('weather-index')
    response = client.get(url)
    assert response.status_code == 200
    assert 'Weather Яeport .' in response.content.decode()
