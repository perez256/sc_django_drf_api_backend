from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework import exceptions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from api.models import User
from api.serializers import UserSerializer, UserSerializerWithToken


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        serializer = UserSerializerWithToken(self.user).data
        for k, v in serializer.items():
            data[k] = v
        if data:
            return data
        else:
            raise exceptions.APIException('Email or Password is invalid')


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


# Get all users
@api_view(['GET'])
@permission_classes([IsAdminUser])
def get_users(incoming):
    user = get_user_model().objects.all()
    serializer = UserSerializer(user, many=True)
    return Response(serializer.data)


@api_view(['PUT'])
# @permission_classes([IsAuthenticated])
def update_user_profile(request):
    user = request.user
    serializer = UserSerializerWithToken(user, many=False)
    data = request.data
    user.first_name = data['first_name']
    user.last_name = data['last_name']
    user.name = data['first_name'] + ' - ' + data['last_name']
    user.contact = data['contact']
    user.username = data['email']
    user.email = data['email']
    try:
        if data['password'] != '':
            user.password = make_password(data['password'])
            print('password', data['password'])
    except Exception as p:
        print(str(p))
        pass
    user.save()
    return Response(serializer.data)


# Get user profile
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_profile(request):
    user = request.user
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)
