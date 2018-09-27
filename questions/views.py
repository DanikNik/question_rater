from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin
from .models import Question, QuestionAnswer
from account.models import Person
from django import forms


class RateForm(forms.Form):
    rating = forms.FloatField()


class QuestionListView(ListView):
    model = Question
    template_name = 'questions/question_list.html'
    context_object_name = 'question_list'


class QuestionDetailView(DetailView, FormMixin):
    model = Question
    template_name = 'questions/question_detail.html'
    context_object_name = 'question'

    form_class = RateForm
    success_url = '/account'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        answer = QuestionAnswer.rate_question(_question=self.get_object(), _rating=form.cleaned_data['rating'], _person=Person.objects.get(id=25))
        answer.save()
        return super(QuestionDetailView, self).form_valid(form)