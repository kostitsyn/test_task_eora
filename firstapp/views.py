from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import CreateAPIView
from .models import DialogItem, Question
from .serializers import DialogSerializer, QuestionSerializer
from rest_framework import mixins
from rest_framework.viewsets import ModelViewSet, GenericViewSet

class DialogAPIViewSet(mixins.RetrieveModelMixin, mixins.CreateModelMixin, GenericViewSet):
    queryset = DialogItem.objects.all()
    serializer_class = DialogSerializer

    def retrieve(self, request, *args, **kwargs):
        data = Question.objects.first()
        serializer = self.serializer_class(data)
        return Response(serializer.data)

class DialogAPIView(APIView):
    serializer_class = DialogSerializer

    def post(self, request):
        serializer = DialogSerializer()
        return Response(status=status.HTTP_200_OK)


class ArticleCreateAPIView(CreateAPIView):
    queryset = DialogItem.objects.all()
    serializer_class = DialogSerializer
