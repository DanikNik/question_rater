from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin
from .models import Question, QuestionAnswers
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['question_answers'] = QuestionAnswers.objects.filter(question=self.object)
            context["user_answer"]= QuestionAnswers.objects.get(person=self.request.user.person, question=self.object)
        finally:
            return context
    def get_success_url(self):
        return self.object.get_absolute_url()

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        answer = QuestionAnswers.rate_question(_question=self.get_object(),
                                               _rating=form.cleaned_data['rating'],
                                               _person=self.request.user.person)
        answer.save()
        return super(QuestionDetailView, self).form_valid(form)