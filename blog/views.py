from rest_framework.response import Response

from blog.filters import NewsFilter
from blog.serializers import NewsSerializer, FavoriteSerializer, NewsDetailSerializer, CommentSerializer
from blog.models import News, Favorite, Comment
from rest_framework import viewsets, generics
from django_filters import rest_framework as filters


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = NewsFilter

    def perform_create(self, serializer):
        request = serializer.context['request']
        serializer.save(author=request.user)

    def retrieve(self, request, pk=None):
        serializer_class = NewsDetailSerializer
        instance = self.get_object()
        return Response(serializer_class(instance).data)


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


# class CommentCreateAPIView(generics.CreateAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
#
#     def create(self, request, *args, **kwargs):
#         user = request.user
#
    # def perform_create(self, serializer):
    #     request = serializer.context['request']
    #     try:
    #         parent = serializer.validated_data['parent']
    #     except:
    #         parent = None
    #
    #     new_comment = Comment(user=request.user, parent=parent)
    #     new_comment.save()
