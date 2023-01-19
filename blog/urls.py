from django.urls import path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('article', viewset=views.NewsViewSet, basename='article')


urlpatterns = [
    path('article/comment/', views.CommentCreateAPIView.as_view(), name='article_comment'),
    path('myarticle/', views.MyArticleListAPIView.as_view(), name='my_article'),
    path('favorite/', views.FavoriteViewSet.as_view(), name='my_favorite'),
]

urlpatterns += router.urls
