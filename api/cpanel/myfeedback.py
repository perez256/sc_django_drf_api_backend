from rest_framework import exceptions
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import FeedBack
from api.serializers import FeedbackSerializer


@api_view(['POST', 'GET'])
def register_comment(incoming):
    if incoming.method == 'POST':
        data = incoming.data
        try:
            feedback = FeedBack.objects.create(
                bussiness_name=data['bussiness_name'],
                comment=data['comment'],
                contact=data['contact'],
                employee_name=data['employee_name'],
                file=data['file'],
                location=data['location'],
                name=data['name'],
            )
            serializer = FeedbackSerializer(feedback, many=False)
            return Response(serializer.data)
        except Exception as p:
            print(str(p))
            raise exceptions.APIException('some thing went wrong please try again')
    if incoming.method == 'GET':
        all_feedback = FeedBack.objects.all()
        serializer = FeedbackSerializer(all_feedback, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def detail_feedback(incoming, pk):
    try:
        feedback_data = FeedBack.objects.get(id=pk)
        serializer = FeedbackSerializer(feedback_data, many=False)
        return Response(serializer.data)
    except Exception as p:
        print(str(p))
        raise exceptions.APIException('Some thing went wrong please try again')


def delete_feedback(incoming, pk):
    try:
        FeedBack.objects.get(id=pk).delete()
        feedback_data = FeedBack.objects.all()
        serializer = FeedbackSerializer(feedback_data, many=True)
        return Response(serializer.data)
    except Exception as p:
        print(str(p))
        raise exceptions.APIException('Some thing went wrong please try again')
