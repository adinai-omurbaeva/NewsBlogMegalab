from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import generics, status
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from accounts.serializers import UserSerializer, RegisterSerializer, ChangePasswordSerializer


User = get_user_model()


class DetailUserApiView(APIView):
    def get(self, request):
        user = request.user
        serialized_user = UserSerializer(user).data
    
        return Response(serialized_user)

    def patch(self, request):
        user = User.objects.get(id=request.user.id)
        serializer = UserSerializer(instance=user, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'msg': 'User profile is updated', 'data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'msg': 'Wrong parameters'})


class RegisterUserAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class ChangePasswordView(APIView):
    def post(self, request):
        serializer = ChangePasswordSerializer(data=request.data, context={'user':request.user})
        serializer.is_valid(raise_exception=True)
        serializer.update_password(serializer.validated_data)
        return Response({"msg": "Password is updated"}, status=status.HTTP_200_OK)
