from core.models import *

from django.contrib.auth.models import User
from rest_framework import serializers


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ["questionText", "questionType", "orderNumber", "answer"]

    def create(self, validated_data):
        validated_data['questionnaire'] = self.context['questionnaire']
        return super(QuestionSerializer, self).create(validated_data)


class QuestionnaireSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Questionnaire
        fields = ["endDateTime", "startDateTime", "title", "description", 'id']


class QuestionnaireSerializerWithoutStartDate(QuestionnaireSerializer):
    """Use this serializer when dealing with any actions other than create"""
    class Meta(QuestionnaireSerializer.Meta):
        read_only_fields = ["startDateTime", "id"]


class QuestionnaireInstanceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = QuestionnaireInstance
        fields = ["answers", "userId", "questionnaireId"]


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']
