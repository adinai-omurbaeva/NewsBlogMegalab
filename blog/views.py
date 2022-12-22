from blog.filters import NewsFilter
from blog.serializers import NewsSerializer, FavoriteSerializer
from blog.models import News, Favorite
from rest_framework import viewsets
from django_filters import rest_framework as filters


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = NewsFilter

    def perform_create(self, serializer):
        request = serializer.context['request']
        serializer.save(author=request.user)


class FavoriteViewSet(viewsets.ModelViewSet):
    serializer_class = FavoriteSerializer
    queryset = Favorite.objects.all()

    def perform_create(self, serializer):
        request = serializer.context['request']
        news = serializer.validated_data['news']
        instance = Favorite.objects.filter(user=request.user, news=news)
        if instance:
            instance.delete()
        else:
            serializer.save(user=request.user)

    def get_queryset(self):
        user = self.request.user
        queryset = Favorite.objects.filter(user=user)
        return queryset
