from rest_framework import exceptions
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import BookRide, User
from api.serializers import BookRideSerializer


@api_view(['POST'])
def order_ride(incoming):
    if incoming.method == 'POST':
        data = incoming.data
        try:
            user = User.objects.get(id=data['user'])
            order_ride_data = BookRide.objects.create(
                user=user,
                name=data['name'],
                ride_type=data['ride_type'],
                address_from=data['address_from'],
                address_to=data['address_to']
            )
            serializer = BookRideSerializer(order_ride_data, many=False)
            return Response(serializer.data)
        except Exception as p:
            print(str(p))
            raise exceptions.APIException('some thing went wrong please try again')
    else:
        raise exceptions.APIException('Invalid Method, please try again')


