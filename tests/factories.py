import factory
from django.contrib.auth.models import User
from blog.models import News, NewsCategory, Comment

from faker import Faker
fake = Faker()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create = ('username',)

    username = fake.user_name()
    is_staff = True
    password = 'TestPass123'
    last_name = fake.last_name()
    first_name = fake.first_name()


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = NewsCategory
    name = fake.word()


class NewsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = News

    title = fake.sentence()
    category = factory.SubFactory(CategoryFactory)
    description = fake.text()
    text = fake.text()
    author = factory.SubFactory(UserFactory)


class CommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Comment

    author = factory.SubFactory(UserFactory)
    news = factory.SubFactory(NewsFactory)
    content = fake.text()


