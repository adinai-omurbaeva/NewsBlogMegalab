from django.urls import path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('article', viewset=views.NewsViewSet)
router.register('favorite', viewset=views.FavoriteViewSet)


urlpatterns = [
    path('article/comment', views.CommentCreateAPIView.as_view()),
]

urlpatterns += router.urls
