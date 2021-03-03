from django.db import models

QUESTION_TYPE_CHOICES = [("TEXT_ANSWER", "Text answer"), ("MULTIPLE_CHOICE", "Multiple choice"),
                         ("MULTIPLE_RESPONSE", "Multiple response")]
ANSWER_TEXT_MAX_LENGTH = 10000  # 10k


class Questionnaire(models.Model):
    startDateTime = models.DateTimeField()
    endDateTime = models.DateTimeField()
    title = models.CharField(max_length=100, blank=False, default='Unnamed questionnaire')
    description = models.TextField()

    class Meta:
        ordering = ['startDateTime']


class Question(models.Model):
    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE)

    questionText = models.TextField()
    questionType = models.CharField(max_length=100, choices=QUESTION_TYPE_CHOICES)  # Reasonable max_length
    orderNumber = models.IntegerField(unique=True)

    answer = models.TextField(max_length=ANSWER_TEXT_MAX_LENGTH)
    # Use as default answer for creating questionnaires
    # No validation for answers in choice questions, as it was not requested in the task

    class Meta:
        ordering = ["questionText"]
