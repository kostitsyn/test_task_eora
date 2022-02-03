from rest_framework import serializers
from .models import Spam

class MainSerializer(serializers.Serializer):
    score = serializers.IntegerField()

    class Meta:
        fields = ('score', )

# class MainSerializer(serializers.ModelSerializer):
#     score1 = serializers.IntegerField()
#
#     class Meta:
#         model = Spam
#         fields = ('score1', )