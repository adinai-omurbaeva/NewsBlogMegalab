from pytest_factoryboy import register
from tests.factories import UserFactory, CategoryFactory, NewsFactory
import pytest

register(UserFactory)
register(CategoryFactory)
register(NewsFactory)


@pytest.fixture()
def new_user(db, user_factory):
    user = user_factory.create()
    return user


@pytest.fixture()
def new_category(db, category_factory):
    category = category_factory.create()
    return category


@pytest.fixture()
def new_news(db, news_factory):
    news = news_factory.create()
    return news
