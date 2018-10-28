from django.views.generic import TemplateView, ListView
from catalog.assets.user_check_mixins import StaffCheckMixin
from questions import models as question_models


class CockpitIndexView(ListView):
    model = question_models.Question
    template_name = 'cockpit/index.html'
    context_object_name = 'question_list'


class CreateQuestionView():
    pass


class CreateTagView():
    pass
