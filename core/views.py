import datetime

from rest_framework.response import Response
from django.contrib.auth.models import User

from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework import permissions
from core.serializers import UserSerializer, QuestionnaireSerializer, QuestionSerializer,\
    QuestionnaireSerializerWithoutStartDate

from core.models import Questionnaire, Question


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class QuestionnaireViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows questionnaires to be viewed or edited.
    """
    # serializer_class =
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Questionnaire.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return QuestionnaireSerializer
        else:
            return QuestionnaireSerializerWithoutStartDate

    def get_queryset(self):
        """Only get active questionnaires for non-staff users"""
        if self.request.user.is_staff:
            return Questionnaire.objects.all()
        else:
            return Questionnaire.objects.filter(startDateTime__lte=datetime.datetime.now(),
                                                endDateTime__gte=datetime.datetime.now())


class QuestionViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionSerializer

    def get_queryset(self):
        return Questionnaire.objects.get(pk=self.kwargs['questionnaire_pk']).questions.all()

    def get_serializer_context(self):
        return {"questionnaire": Questionnaire.objects.get(pk=self.kwargs['questionnaire_pk'])}