from .models import DialogItem, Question
from rest_framework import serializers


class DialogSerializer(serializers.ModelSerializer):
    user_id = serializers.CharField(max_length=64)
    message = serializers.CharField(max_length=64, default='')

    class Meta:
        model = DialogItem
        fields = ('user_id', 'message')


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('text_question',)
