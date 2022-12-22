from django.urls import path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('article', viewset=views.NewsViewSet)
router.register('favorite', viewset=views.FavoriteViewSet)

urlpatterns = [
    
]

urlpatterns += router.urls
