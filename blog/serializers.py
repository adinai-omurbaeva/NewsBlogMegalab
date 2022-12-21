from rest_framework import serializers
from blog.models import News


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('title', 'theme', 'image', 'text', 'date', 'author')