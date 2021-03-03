from core.models import Questionnaire, Question

from django.contrib.auth.models import User
from rest_framework import serializers


class QuestionnaireSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Questionnaire
        fields = ["startDateTime", "endDateTime", "title", "description"]


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ["startDateTime", "endDateTime", "title", "description"]


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


