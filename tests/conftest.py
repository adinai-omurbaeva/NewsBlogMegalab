from pytest_factoryboy import register
from tests.factories import CategoryFactory, NewsFactory, UserFactory
import pytest

register(UserFactory)
register(CategoryFactory)
register(NewsFactory)


@pytest.fixture()
def test_user(db, user_factory):
    user = user_factory.create()
    user.set_password("TestPass123")
    user.save()
    return user


@pytest.fixture()
def test_category(db, category_factory):
    category = category_factory.create()
    return category


@pytest.fixture()
def test_news(db, news_factory):
    news = news_factory.create()
    return news
