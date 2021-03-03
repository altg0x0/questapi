from core.models import Questionnaire, Question

from django.contrib.auth.models import User
from rest_framework import serializers


class QuestionnaireSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Questionnaire
        fields = ["endDateTime", "startDateTime", "title", "description"]


class QuestionnaireSerializerWithoutStartDate(QuestionnaireSerializer):
    """Use this serializer when dealing with any actions other than create"""
    class Meta:
        model = Questionnaire
        read_only_fields = ["startDateTime", ]
        fields = ["endDateTime", "startDateTime", "title", "description"]


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


