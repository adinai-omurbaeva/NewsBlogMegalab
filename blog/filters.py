import django_filters

from blog.models import News


class NewsFilter(django_filters.FilterSet):
    category = django_filters.CharFilter(field_name='category__name', lookup_expr='iexact')

    class Meta:
        model = News
        fields = ['category']

