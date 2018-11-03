from django.views.generic import ListView, DetailView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import FormMixin
from .models import Question, QuestionAnswer, QuestionAnswersLog, Tag
from django.db import models
from account.models import Person
from django import forms
from catalog.assets.user_check_mixins import ProfileCheckMixin


class RateForm(forms.Form):
    rating = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}))


class QuestionListView(ProfileCheckMixin, ListView):
    model = Question
    template_name = 'questions/question_list.html'
    # paginate_by = 4
    # context_object_name = 'question_list'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        tag_name = self.request.GET.get('tag')
        if tag_name is not None:
            context['tag_query'] = tag_name
            context['question_list'] = Question.objects.filter(tags__tag_name__exact=tag_name)
        else:
            context['question_list'] = Question.objects.all()
        return context


class QuestionDetailView(ProfileCheckMixin, DetailView, FormMixin):
    model = Question
    template_name = 'questions/question_detail.html'
    context_object_name = 'question'

    form_class = RateForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['question_answers'] = QuestionAnswer.objects.filter(question=self.object).order_by('person')

            context["user_latest_answer"] = QuestionAnswersLog.objects.filter(person=self.request.user.person,
                                                                              question=self.object).latest('timestamp')
            context['user_answers'] = QuestionAnswersLog.objects.filter(person=self.request.user.person,
                                                                        question=self.object).order_by('-timestamp')
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
        answer = QuestionAnswersLog.rate_question(_question=self.get_object(),
                                                  _rating=form.cleaned_data['rating'],
                                                  _person=self.request.user.person)
        answer.save()
        try:
            prev_answer = QuestionAnswer.objects.get(person=self.request.user.person,
                                                     question=self.object)
            prev_answer.set_log_entry(answer)
        except:
            QuestionAnswer.objects.create(person=self.request.user.person, question=self.object, log=answer)

        return super(QuestionDetailView, self).form_valid(form)

# class QuestionByTagListView(QuestionListView, SingleObjectMixin):
#     model = Tag
#     slug_field = 'tag_name'
#
#     def get_object(self, queryset=None):
#         id = self.request.pk
#         return Tag.objects.get(id=id)
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['question_list'] = Question.objects.filter(tags__in=self.get_object())
