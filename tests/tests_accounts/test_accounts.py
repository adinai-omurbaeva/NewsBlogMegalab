import json

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


# @pytest.mark.django_db
# def test_login(new_user):
#     data = {'username': new_user.username, 'password': new_user.password}
#     client.force_authenticate(user=new_user)
#     response = client.post(reverse('token_obtain_pair'), data, headers={'Content-type': 'application/json'})
#     assert response.status_code==201


@pytest.mark.django_db
# def test_change_password(new_user):
#     url = reverse('change_password')
#     data = json.dumps({'old_password': 'TestPass123',
#             'password': 'NewPass123',
#             'password2': 'NewPass123'
#             })
#     client.force_authenticate(user=new_user)
#     response = client.post(url, data, headers={'Content-type': 'application/json'})
#     assert response.status_code == 201


@pytest.mark.django_db
def test_profile(new_user):
    url = reverse('profile_user')
    client.force_authenticate(new_user)
    responce = client.get(url)
    assert responce.status_code==200