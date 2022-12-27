from django.contrib import admin
from blog.models import News, Favorite, NewsCategory, Comment

admin.site.register(News)
admin.site.register(Comment)
admin.site.register(NewsCategory)
admin.site.register(Favorite)
