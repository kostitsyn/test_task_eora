import csv
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import MainSerializer
from .models import Spam
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer


class MainAPIView(APIView):
    serializer_class = MainSerializer
    # renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

    def get(self, request, format=None):
        data = Spam.objects.all()
        # with open('table.csv') as f:
        #     data = csv.reader(f)
        #     print()
        serializer = MainSerializer(data, many=True)
        data = {'score': ''}
        # return Response(serializer.data)
        # return Response(status=status.HTTP_200_OK)
        return Response(serializer.data)

    def post(self, request):
        print()
        data = {'score': ''}
        return Response(data)


