from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from blog.models import News, Favorite


class NewsSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    author = serializers.StringRelatedField(default=serializers.CurrentUserDefault(), read_only=True)

    class Meta:
        model = News
        fields = ('id', 'title', 'category_name', 'category', 'image', 'text', 'date', 'author')


class FavoriteSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(default=serializers.CurrentUserDefault(), read_only=True)

    class Meta:
        model = Favorite
        fields = ('user', 'news')
        # validators = [
        #     UniqueTogetherValidator(
        #         queryset=Favorite.objects.all(),
        #         fields=['user', 'news']
        #     )
        # ]

    def get_request(self, user):
        queryset = Favorite.objects.filter(user=user)
        return queryset
