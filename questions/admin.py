from django.contrib import admin
from . import models

admin.site.register(models.Question)
admin.site.register(models.QuestionAnswer)
admin.site.register(models.QuestionAnswersLog)
# admin.site.register(models.Tag)