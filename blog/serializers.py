from rest_framework import serializers
from blog.models import News


class NewsSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name')
    class Meta:
        model = News
        fields = ('title', 'category_name', 'image', 'text', 'date', 'author')