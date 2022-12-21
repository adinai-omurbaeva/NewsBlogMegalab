from django.db import models
from accounts.models import User


class NewsCategory(models.Model):
    name = models.CharField(max_length=255)


class News(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(NewsCategory, on_delete=models.CASCADE)
    # theme = models.CharField(max_length=255, default='')
    image = models.ImageField()
    text = models.CharField(max_length=255)
    date = models.DateField(auto_now=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


class Comment(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    date = models.DateField(auto_now=True, blank=True)


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    news = models.ForeignKey(News, on_delete=models.CASCADE)