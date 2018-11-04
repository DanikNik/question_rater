from django import forms
from django.core.mail import send_mail


class QuestionSetAnswerForm(forms.Form):
    answer = forms.BooleanField(label='Is True?')

    # @property
    # def email_subject_template(self):
    #     return 'email/account/notification_subject.txt'
    #
    # @property
    # def email_body_template(self):
    #     raise NotImplementedError()

    def form_action(self, question):
        # print(question)
        return question.rebase_user_ratings()

    def save(self, question):
        # print(question)
        question.true_answer = self.cleaned_data['answer']
        question.save()
        # print(self.cleaned_data['answer'])
        self.form_action(question)