from django.urls import path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('article', viewset=views.NewsViewSet)


urlpatterns = [
    path('article/comment/', views.CommentCreateAPIView.as_view()),
    path('myarticle/', views.MyArticleListAPIView.as_view()),
    path('favorite/', views.FavoriteViewSet.as_view()),
]

urlpatterns += router.urls
