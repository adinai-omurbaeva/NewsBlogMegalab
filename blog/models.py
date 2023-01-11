from django.db import models
from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class NewsCategory(models.Model):
    name = models.CharField(max_length=255)


class News(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(NewsCategory, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='static/images/')
    text = models.CharField(max_length=255)
    date = models.DateField(auto_now=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    content = models.CharField(max_length=255)
    date_posted = models.DateField(auto_now_add=True, blank=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')

    class Meta:
        ordering = ['-date_posted']

    def __str__(self):
        return str(self.user) + ' comment ' + str(self.content)


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    news = models.ForeignKey(News, on_delete=models.CASCADE)
