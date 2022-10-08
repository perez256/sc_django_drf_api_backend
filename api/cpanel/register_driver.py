from django.contrib.auth.hashers import make_password
from rest_framework import exceptions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import User
from api.serializers import UserSerializer, UserSerializerWithToken


@api_view(['POST'])
def register_driver(incoming):
    data = incoming.data
    user = User.objects.create(
        first_name=data['first_name'],
        last_name=data['last_name'],
        email=data['email'],
        username=data['email'],
        contact=data['contact'],
        password=make_password(data['password']),
        is_driver=True,
    )
    serializer = UserSerializerWithToken(user, many=False)
    return Response(serializer.data)
