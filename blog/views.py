from blog.filters import NewsFilter
from blog.serializers import NewsSerializer
from blog.models import News
from rest_framework import viewsets
from django_filters import rest_framework as filters


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = NewsFilter
