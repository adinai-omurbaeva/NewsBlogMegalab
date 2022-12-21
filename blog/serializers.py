from rest_framework import serializers
from blog.models import News


class NewsSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    author = serializers.StringRelatedField(default=serializers.CurrentUserDefault(), read_only=True)

    class Meta:
        model = News
        fields = ('title', 'category_name', 'category', 'image', 'text', 'date', 'author')

