import datetime

from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from core.serializers import UserSerializer, QuestionnaireSerializer

from core.models import Questionnaire


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class QuestionnaireViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    serializer_class = QuestionnaireSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Questionnaire.objects.all()

    def get_queryset(self):
        """Only get active questionnaires for non-staff users"""
        if self.request.user.is_staff:
            return Questionnaire.objects.all()
        else:
            return Questionnaire.objects.filter(startDateTime__lte=datetime.datetime.now(),
                                                endDateTime__gte=datetime.datetime.now())
