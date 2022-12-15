from accounts.views import DetailUserApiView, login_view, RegisterUserAPIView
from django.urls import path


urlpatterns = [
    path('detail', DetailUserApiView.as_view()),
    path('login', login_view, name='login'),
    path('register',RegisterUserAPIView.as_view()),
]