from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import generics
from rest_framework.views import APIView

from accounts.serializers import UserSerializer, RegisterSerializer


class DetailUserApiView(APIView):
    def get(self, request):
        user = request.user
        serialized_user = UserSerializer(user).data
    
        return Response(serialized_user)


class RegisterUserAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

