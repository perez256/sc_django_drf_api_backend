from rest_framework import exceptions
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import ResearchLab
from api.serializers import ResearchLabSerializer


@api_view(['POST', 'GET'])
def research(incoming):
    if incoming.method == 'POST':
        data = incoming.data
        try:
            research_data = ResearchLab.objects.create(
                business_name=data['business_name'],
                contact=data['contact'],
                address=data['address']
            )
            serializer = ResearchLabSerializer(research_data, many=False)
            return Response(serializer.data)
        except Exception as p:
            print(str(p))
            raise exceptions.APIException('some thing went wrong please try again')
    if incoming.method == 'GET':
        research_data = ResearchLab.objects.all()
        serializer = ResearchLabSerializer(research_data, many=True)
        return Response(serializer.data)
