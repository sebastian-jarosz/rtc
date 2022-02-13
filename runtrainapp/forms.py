from allauth.account.forms import AddEmailForm
from allauth.account.models import EmailAddress
from django import forms
from runtrainapp.managers.data_manager import *
from datetime import datetime


def get_current_date_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# Custom Form to block sending confirmation e-mail
class CustomAddEmailForm(AddEmailForm):
    def save(self, request):
        return EmailAddress.objects.add_email(
            request, self.user, self.cleaned_data["email"], confirm=False
        )


class AddTrainingForm(forms.Form):
    start_date = forms.DateTimeField(initial=get_current_date_time)
    training_time = forms.IntegerField(label='Training time (in minutes)')
    training_type = forms.ChoiceField()
    user = forms.ChoiceField(disabled=True)

    def __init__(self, training_types, users, is_admin=False):
        super().__init__()
        self['training_type'].field.choices = training_types
        self['user'].field.choices = users

        # Enable field for admin
        if is_admin:
            self['user'].field.disabled = False



