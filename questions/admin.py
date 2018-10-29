from django.contrib import admin
from . import models

# admin.site.register(models.Question)
# admin.site.register(models.QuestionAnswer)
# admin.site.register(models.QuestionAnswersLog)
admin.site.register(models.Tag)


class QuestionTag(admin.TabularInline):
    model = models.Tag
    extra = 1


@admin.register(models.Question)
class Question(admin.ModelAdmin):
    model = models.Question
    inlines = [QuestionTag, ]
