from rest_framework.views import APIView
from rest_framework.response import Response
from blog.filters import NewsFilter
from blog.serializers import NewsSerializer, FavoriteSerializer, NewsDetailSerializer, CommentSerializer
from blog.models import News, Favorite, Comment
from rest_framework import viewsets, generics, filters as s_filters
from django_filters import rest_framework as filters
from .utils import RequestUser


class NewsViewSet(RequestUser, viewsets.ModelViewSet):
    queryset = News.objects.all().order_by('-date')
    serializer_class = NewsSerializer
    filter_backends = (filters.DjangoFilterBackend, s_filters.SearchFilter)
    filterset_class = NewsFilter
    search_fields = ['title']

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return NewsDetailSerializer
        return self.serializer_class


class FavoriteViewSet(APIView):
    def get(self, request):
        user = self.request.user
        queryset = News.objects.filter(favorite_news__user=user)
        serializer = NewsSerializer(queryset, many=True, context={'request':request})
        return Response(serializer.data)

    def post(self, request):
        user = request.user
        news_data = {'news':request.data.get('news'), 'user':user.id}
        serializer = FavoriteSerializer(data=news_data)
        serializer.is_valid(raise_exception=True)
        favorite_news = Favorite.objects.filter(**news_data)
        if favorite_news.exists():
            favorite_news.delete()
        else:
            serializer.save()
        return Response(serializer.data)


class CommentCreateAPIView(RequestUser, generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class MyArticleListAPIView(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = News.objects.filter(author=user)
        return queryset
