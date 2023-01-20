from rest_framework.test import APIClient
from django.urls import reverse
import pytest
from faker import Faker

client = APIClient()
fake = Faker()


@pytest.mark.django_db
def test_news_list(test_user):
    url = reverse('article-list')
    client.force_authenticate(test_user)
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_news_create(test_user, test_category):
    url = reverse('article-list')
    client.force_authenticate(test_user)
    data = {
        'title': fake.sentence(),
        "category": test_category.id,
        "description": fake.text(),
        "text": fake.text(),
    }
    response = client.post(url, data=data, format='json')
    assert response.status_code == 201


@pytest.mark.django_db
def test_news_delete(test_user, test_news):
    url = reverse('article-detail', kwargs={'pk': test_news.id})
    client.force_authenticate(test_user)
    response = client.delete(url)
    assert response.status_code == 204


@pytest.mark.django_db
def test_get_news_detail(test_news, test_user):
    url = reverse('article-detail', kwargs={'pk': test_news.id})
    client.force_authenticate(test_user)
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_my_news(test_user):
    url = reverse('my_article')
    client.force_authenticate(test_user)
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_favorite_news(test_user):
    url = reverse('my_favorite')
    client.force_authenticate(test_user)
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_update_news(test_news, test_user):
    url = reverse('article-detail', kwargs={'pk': test_news.id})
    data = {
        'title':'new title'
    }
    client.force_authenticate(test_user)
    response = client.patch(url, data, forman='json')
    assert response.status_code == 200


@pytest.mark.django_db
def test_comment_create(test_user, test_news):
    url = reverse('article_comment')
    client.force_authenticate(test_user)
    data = {
        'author': test_user.id,
        'content': fake.text(),
        'news': test_news.id
    }
    response = client.post(url, data=data, format='json')
    assert response.status_code == 201

