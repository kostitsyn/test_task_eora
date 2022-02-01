from .models import DialogItem, Question
from rest_framework import serializers


# class StartSerializer(serializers.Serializer):
#     user_id = serializers.CharField(max_length=64)
#     message = serializers.CharField(max_length=64)

class DialogSerializer(serializers.ModelSerializer):
    message = serializers.CharField(max_length=64)

    class Meta:
        model = DialogItem
        fields = ('user_id', 'message')


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('text_question',)