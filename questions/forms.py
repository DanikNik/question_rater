from django import forms
from django.core.mail import send_mail

class QuestionActionForm(forms.Form):
    comment = forms.CharField(
        required=False,
        widget=forms.Textarea,
    )
    send_email = forms.BooleanField(
        required=False,
    )

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
        if self.cleaned_data.get('send_email', False):
            send_mail(
                recipient_list=[account.user.email],
                subject=self.email_subject_template,
                html_message=self.email_body_template,
                context={
                    "account": account,
                    "action": action,
                }
            )

        return account, action