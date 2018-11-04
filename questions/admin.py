from django.conf.urls import url
from django.contrib import admin
from . import models
from django.utils.html import format_html
from django.urls import reverse, path
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse

from .forms import QuestionSetAnswerForm

# admin.site.register(models.Question)
# admin.site.register(models.QuestionAnswer)
# admin.site.register(models.QuestionAnswersLog)
admin.site.register(models.Tag)


class TagsInline(admin.StackedInline):
    verbose_name = 'Tag'
    model = models.Question.tags.through
    extra = 1


@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
    exclude = ['tags']
    inlines = [
        TagsInline,
    ]
    list_display = (
        # 'id',
        'title',
        'question_actions',
        'is_expired',
        'true_answer'
    )


    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                '<question_id>/set-answer/',
                self.admin_site.admin_view(self.set_answer),
                name='question-set-answer',
            ),
        ]
        return custom_urls + urls

    def question_actions(self, obj):
        return format_html(
            '<a class="button" href="{}">Set Answer</a>&nbsp;',
            reverse('admin:question-set-answer', args=[obj.pk]),
        )

    question_actions.short_description = 'Question Actions'
    question_actions.allow_tags = True

    def set_answer(self, request, question_id, *args, **kwargs):
        return self.process_action(
            request=request,
            question_id=question_id,
            action_form=QuestionSetAnswerForm,
            action_title='Set Answer',
        )

    def process_action(
            self,
            request,
            question_id,
            action_form,
            action_title
    ):
        question = self.get_object(request, question_id)

        if request.method != 'POST':
            form = action_form()

        else:
            form = action_form(request.POST)
            if form.is_valid():
                form.save(question)

                self.message_user(request, 'Success')
                url = reverse(
                    "admin:questions_question_change",
                    args=[question.pk],
                    current_app=self.admin_site.name,
                )
                return HttpResponseRedirect(url)

        context = self.admin_site.each_context(request)
        context['opts'] = self.model._meta
        context['form'] = form
        context['question'] = question
        context['title'] = action_title

        return TemplateResponse(
            request,
            'admin/question/question_action.html',
            context,
        )
