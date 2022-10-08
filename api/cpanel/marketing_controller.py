from rest_framework import exceptions
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Marketing
from api.serializers import MarketingSerializer


@api_view(['POST', 'GET'])
def marketing(incoming):
    if incoming.method == 'POST':
        data = incoming.data
        try:
            market_data = Marketing.objects.create(
                name=data['name'],
                contact=data['contact'],
                address=data['address']
            )
            serializer = MarketingSerializer(market_data, many=False)
            return Response(serializer.data)
        except Exception as p:
            print(str(p))
            raise exceptions.APIException('some thing went wrong please try again')
    if incoming.method == 'GET':
        market_data = Marketing.objects.all()
        serializer = MarketingSerializer(market_data, many=True)
        return Response(serializer.data)
