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
    training_time = forms.IntegerField(label='Training time (in minutes)', min_value=1)
    training_type = forms.ChoiceField()
    user = forms.ChoiceField(disabled=True)

    def __init__(self, training_types, users, is_admin=False):
        super().__init__()
        self['training_type'].field.choices = training_types
        self['user'].field.choices = users

        # Enable field for admin
        if is_admin:
            self['user'].field.disabled = False


class AddRunningTrainingForm(forms.Form):
    # Training part
    start_date = forms.DateTimeField(initial=get_current_date_time)
    training_time = forms.IntegerField(label='Training time (in minutes)', min_value=1)
    user = forms.ChoiceField(disabled=True)

    # Running Training part
    distance = forms.DecimalField(label='Distance (in meters)', min_value=0.1, decimal_places=2)
    # Segments - Default value 1
    segments_amount = forms.IntegerField(label='Segments amount', initial=1, min_value=1)
    running_training_type = forms.ChoiceField()

    def __init__(self, users, running_training_types, is_admin=False):
        super().__init__()
        self['user'].field.choices = users
        self['running_training_type'].field.choices = running_training_types

        # Enable field for admin
        if is_admin:
            self['user'].field.disabled = False


