from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView
from catalog.assets.user_check_mixins import StaffCheckMixin
from questions import models as question_models


from questions.models import Question

class CockpitIndexView(StaffCheckMixin, ListView):
    model = question_models.Question
    template_name = 'cockpit/index.html'
    context_object_name = 'question_list'

# DEPRECATED

# class CreateQuestionView(StaffCheckMixin, CreateView):
#     template_name = "cockpit/question_create.html"
#     model = Question
#     fields = ['title',
#               'description',
#               'tags']
#
# class CreateTagView(StaffCheckMixin):
#     pass
#