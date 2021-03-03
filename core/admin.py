from django.contrib import admin

from core.models import Questionnaire


class QuestionnaireAdmin(admin.ModelAdmin):
    pass


# Register your models here.
admin.site.register(Questionnaire, QuestionnaireAdmin)
