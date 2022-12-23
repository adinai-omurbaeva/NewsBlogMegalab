from rest_framework import serializers
from blog.models import News, Favorite, Comment


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

    def get_request(self, user):
        queryset = Favorite.objects.filter(user=user)
        return queryset


class CommentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    reply = serializers.SerializerMethodField('get_reply', read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'username', 'news', 'content', 'date_posted', 'parent', 'reply')

    def get_reply(self, new_comment):
        my_comment = Comment.objects.filter(parent=new_comment)
        final_comment = CommentSerializer(instance=my_comment, many=True)
        return final_comment.data


class NewsDetailSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='author.username', read_only=True)
    category_name = serializers.CharField(source='category.name', read_only=True)
    comments = serializers.SerializerMethodField('get_comments')

    class Meta:
        model = News
        fields = ('id', 'title', 'category_name', 'category', 'image', 'text', 'date', 'username', 'comments')

    def get_comments(self, article):
        my_comment = Comment.objects.filter(news=article, parent=None)
        final_comment = CommentSerializer(instance=my_comment, many=True)
        return final_comment.data
