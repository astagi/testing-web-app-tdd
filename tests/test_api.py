import pytest
from django.urls import reverse


def test_api(client):
    response = client.get('/api/temperature?city=Pistoia')
    assert response.status_code == 200


def test_api_on_error(client):
    response = client.get('/api/temperature?city=')
    assert response.status_code == 500
