from rest_framework.test import APIClient
from django.urls import reverse
import pytest
from faker import Faker

client = APIClient()
fake = Faker()


@pytest.mark.django_db
def test_create_user():
    url = reverse('register_user')
    data = {
        'username': 'user',
        'password': 'TestPass123',
        'password2': 'TestPass123',
        'last_name': 'user',
        "first_name": 'user'
    }
    response = client.post(url, data)
    assert response.status_code == 201


@pytest.mark.django_db
def test_login(test_user):
    data = {'username': test_user.username, 'password': "TestPass123"}
    response = client.post(reverse('token_obtain_pair'), data, format='json')
    assert response.status_code == 200


@pytest.mark.django_db
def test_profile(test_user):
    url = reverse('profile_user')
    client.force_authenticate(test_user)
    responce = client.get(url)
    assert responce.status_code == 200
