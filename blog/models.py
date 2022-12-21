from django.db import models
from accounts.models import User


class News(models.Model):
    THEME_CHOISES = (
        ("sport", 'Спорт'),
        ("politic", 'Политика'),
        ("celebrity", 'Звезды'),
        ("art", 'Искусство'),
        ("fashion", 'Мода'),
    )
    title = models.CharField(max_length=255)
    theme = models.CharField(choices=THEME_CHOISES, max_length=255, verbose_name='Тематика')
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