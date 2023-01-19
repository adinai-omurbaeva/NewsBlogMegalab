from accounts.views import DetailUserApiView, RegisterUserAPIView, ChangePasswordView
from django.urls import path
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    path('profile/', DetailUserApiView.as_view(), name='profile_user'),
    path('register/', RegisterUserAPIView.as_view(), name='register_user'),
    path('login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('change_password/', ChangePasswordView.as_view(), name='change_password'),
]


