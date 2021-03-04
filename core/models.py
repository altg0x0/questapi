from django.db import models

QUESTION_TYPE_CHOICES = [("TEXT_ANSWER", "Text answer"), ("MULTIPLE_CHOICE", "Multiple choice"),
                         ("MULTIPLE_RESPONSE", "Multiple response")]
ANSWER_TEXT_MAX_LENGTH = 10000  # 10k


class Questionnaire(models.Model):
    """Represents a questionnaire, as set of questions and metadata"""
    startDateTime = models.DateTimeField()
    endDateTime = models.DateTimeField()
    title = models.CharField(max_length=100, blank=False, default='Unnamed questionnaire')
    description = models.TextField()

    class Meta:
        ordering = ['startDateTime']


class Question(models.Model):
    questionnaire = models.ForeignKey(Questionnaire, related_name="questions", on_delete=models.CASCADE)

    questionText = models.TextField()
    questionType = models.CharField(max_length=100, choices=QUESTION_TYPE_CHOICES)  # Reasonable max_length
    orderNumber = models.IntegerField()
    answer = models.TextField(max_length=ANSWER_TEXT_MAX_LENGTH, blank=True)
    # Use as default answer for creating questionnaires
    # No validation for answers in choice questions, as it was not requested in the task

    class Meta:
        ordering = ["orderNumber"]


class QuestionnaireInstance(models.Model):
    """Represents a finished questionnaire instance, so one Questionnaire can have multiple instances"""
    questionnaireId = models.IntegerField()  # Could use ForeignKey but mo need to, as we don't validate answers anyway
    userId = models.IntegerField()

    answers = models.TextField(max_length=100000)  # Reasonable choice
    """ IMPORTANT!
        We store answers as unvalidated JSON because we don't have any way to validate them,
        as we don't know the list of possible answers for choice questions. Thus, if users tamper with their answers,
        it's their problem.
    """

    class Meta:
        ordering = ["id"]
