from accounts.views import profile, login_view, RegisterUserAPIView
from django.urls import path
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('profile', profile, name='profile'),
    path('login', login_view, name='login'),
    path('register',RegisterUserAPIView.as_view()),
]