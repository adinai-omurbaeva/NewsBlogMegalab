from rest_framework.exceptions import APIException
from rest_framework.response import Response

from blog.filters import NewsFilter
from blog.serializers import NewsSerializer, FavoriteSerializer, NewsDetailSerializer, CommentSerializer
from blog.models import News, Favorite, Comment
from rest_framework import viewsets, generics
from django_filters import rest_framework as filters


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all().order_by('-date')
    serializer_class = NewsSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = NewsFilter

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return NewsDetailSerializer
        return self.serializer_class


class FavoriteViewSet(viewsets.ModelViewSet):
    serializer_class = FavoriteSerializer
    queryset = Favorite.objects.all()

    def perform_create(self, serializer):
        user = self.request.user
        news = serializer.validated_data['news']
        instance = Favorite.objects.filter(user=user, news=news)
        if instance:
            instance.delete()
        else:
            serializer.save(user=user)

    def get_queryset(self):
        user = self.request.user
        queryset = Favorite.objects.filter(user=user)
        return queryset


class CommentCreateAPIView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

