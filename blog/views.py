from django.shortcuts import render
from blog.serializers import NewsSerializer
from blog.models import News
from rest_framework import generics
from django_filters import rest_framework as filters
import django_filters


class NewsFilter(django_filters.FilterSet):
    # category__name = django_filters.CharFilter(lookup_expr='icontains')
    category = django_filters.CharFilter(field_name='category__name', lookup_expr='iexact')

    class Meta:
        model = News
        # filterset_fields = ('category__name',)
        fields = ['category']


class NewsList(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    # filterset_fields = ('category',)
    filterset_class = NewsFilter
