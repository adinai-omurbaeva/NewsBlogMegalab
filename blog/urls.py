from django.urls import path
from blog.views import NewsList


urlpatterns = [
    path('news', NewsList.as_view()),
    
]