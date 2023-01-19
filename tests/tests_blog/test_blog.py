from rest_framework.test import APIClient
from django.urls import reverse
import pytest
from faker import Faker

client = APIClient()
fake = Faker()


@pytest.mark.django_db
def test_news_list(new_user):
    url = reverse('article-list')
    client.force_authenticate(new_user)
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_news_create(new_user, new_category):
    url = reverse('article-list')
    client.force_authenticate(new_user)
    data = {
        'title': fake.sentence(),
        "category": new_category.id,
        "description": fake.text(),
        "text": fake.text(),
        "author": new_user.id,
    }
    response = client.post(url, data=data, format='json')
    assert response.status_code == 201


@pytest.mark.django_db
def test_article_delete(new_user, new_news):
    url = reverse('article-detail', kwargs={'pk': new_user.id})
    client.force_authenticate(new_user)
    response = client.delete(url)
    assert response.status_code == 204


@pytest.mark.django_db
def test_get_article_detail(new_news, new_user):
    url = reverse('article-detail', kwargs={'pk': new_user.id})
    client.force_authenticate(new_user)
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_my_articles(new_user):
    url = reverse('my_article')
    client.force_authenticate(new_user)
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_favorite_news(new_user):
    url = reverse('my_favorite')
    client.force_authenticate(new_user)
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_comment_create(new_user, new_news):
    url = reverse('article_comment')
    client.force_authenticate(new_user)
    data = {
        'author': new_user.id,
        'content': fake.text(),
        'news': new_news.id
    }
    response = client.post(url, data=data, format='json')
    assert response.status_code == 201

