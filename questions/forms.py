from django import forms
from django.core.mail import send_mail

class QuestionSetAnswerForm(forms.Form):
    answer = forms.BooleanField()

    # @property
    # def email_subject_template(self):
    #     return 'email/account/notification_subject.txt'
    #
    # @property
    # def email_body_template(self):
    #     raise NotImplementedError()

    def form_action(self, account, user):
        raise NotImplementedError()

    def save(self, account, user):
        try:
            account, action = self.form_action(account, user)

        except errors.Error as e:
            error_message = str(e)
            self.add_error(None, error_message)
            raise

        if self.cleaned_data.get('send_email', False):
            send_mail(
                recipient_list=[account.user.email],
                subject=self.email_subject_template,
                body_template=self.email_body_template,
                context={
                    "account": account,
                    "action": action,
                }
            )

        return account, action