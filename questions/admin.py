from django.contrib import admin
from . import models


# admin.site.register(models.Question)
# admin.site.register(models.QuestionAnswer)
# admin.site.register(models.QuestionAnswersLog)
admin.site.register(models.Tag)


class TagsInline(admin.TabularInline):
    model = models.Question.tags.through
    extra = 1


@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
    exclude = ['tags']
    inlines = [
        TagsInline,
    ]
