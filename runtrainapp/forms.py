from allauth.account.forms import AddEmailForm
from allauth.account.models import EmailAddress
from runtrainapp.models import *
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


class GenerateTrainingForm(forms.Form):
    year_of_birth = forms.IntegerField(label='Proszę podać rok urodzenia', min_value=1900, max_value=2022)
    height = forms.IntegerField(label='Proszę podać swój wzrost (w centymetrach)', min_value=100, max_value=250)
    weight = forms.IntegerField(label='Proszę podać swoją wagę (w kilogramach)', min_value=30, max_value=200)
    running_years = forms.IntegerField(label="Od ilu lat regularnie biegasz?", min_value=0, max_value=50)
    training_amount = forms.IntegerField(label="Ile treningów biegowych wykonujesz średnio w ciągu tygodnia?",
                                         min_value=0, max_value=50)
    km_amount = forms.IntegerField(
        label="Ile kilometrów pokonujesz średnio podczas treningów biegowych w ciągu tygodnia?", min_value=0,
        max_value=50)
    speed_training_amount = forms.IntegerField(label="Ile razy w ciągu miesiąca wykonujesz trening szybkości?",
                                               min_value=0, max_value=50)
    minute_per_km_speed_training_id = forms.ChoiceField(
        label="W jakim zakresie tempa wykonujesz trening szybkości? (w minutach na kilometr)")
    threshold_training_amount = forms.IntegerField(label="Ile razy w ciągu miesiąca wykonujesz trening progowy?",
                                                   min_value=0, max_value=50)
    minute_per_km_threshold_training_id = forms.ChoiceField(
        label="W jakim zakresie tempa wykonujesz trening progowy? (w minutach na kilometr)")
    interval_training_amount = forms.IntegerField(label="Ile razy w ciągu miesiąca wykonujesz trening interwałowy?",
                                                  min_value=0, max_value=50)
    minute_per_km_interval_training_id = forms.ChoiceField(
        label="W jakim zakresie tempa wykonujesz trening interwałowy? (w minutach na kilometr)")
    run_up_training_amount = forms.IntegerField(label="Ile razy w ciągu miesiąca wykonujesz podbiegi?", min_value=0,
                                                max_value=50)
    minute_per_km_run_up_training_id = forms.ChoiceField(
        label="W jakim zakresie tempa wykonujesz podbiegi? (w minutach na kilometr)")
    runway_amount = forms.IntegerField(label="Ile razy w ciągu miesiąca wykonujesz wybieganie?", min_value=0,
                                       max_value=50)
    km_per_runway = forms.IntegerField(
        label="Jaka jest średnia ilość kilometrów wykonywana podczas jednego wybiegania?", min_value=0, max_value=50)
    minute_per_km_runway_id = forms.ChoiceField(
        label="W jakim zakresie tempa wykonujesz wybieganie? (w minutach na kilometr)")
    other_trainings = forms.BooleanField(label="Czy wykonujesz treningi inne niż biegowe?", required=False)
    other_trainings_amount = forms.IntegerField(
        label="Ile razy w ciągu miesiąca wykonujesz powyższe treningi? (sumarycznie)")
    other_trainings_time = forms.IntegerField(label="Ile minut średnio trwa pojedynczy trening?", min_value=0,
                                              max_value=50)
    wellness = forms.BooleanField(label="Czy wykonujesz aktywności związane z odnową biologiczną?", required=False)
    wellness_amount = forms.IntegerField(
        label="Ile razy w ciągu miesiąca wykonujesz powyższe aktywności? (sumarycznie)", min_value=0, max_value=50)
    detraining_amount = forms.IntegerField(label="Ile razy w ciągu roku stosujesz roztrenowanie?", min_value=0,
                                           max_value=50)
    detraining_days = forms.IntegerField(label="Jaki jest Twój średni czas trwania roztrenowania? (w dniach)",
                                         min_value=0, max_value=50)
    warmup_id = forms.ChoiceField(label="Czy stosujesz rozgrzewkę przed treningiem biegowym?")
    warmup_time = forms.IntegerField(label="Jaki jest średni czas trwania rozgrzewki? (w minutach)", min_value=0,
                                     max_value=50)

    def __init__(self):
        super().__init__()
        self.base_fields['minute_per_km_speed_training_id'].choices = get_training_timing_description_list([TIMING_9, TIMING_10, TIMING_12])
        self.base_fields['minute_per_km_threshold_training_id'].choices = get_training_timing_description_list([TIMING_9, TIMING_10, TIMING_12])
        self.base_fields['minute_per_km_interval_training_id'].choices = get_training_timing_description_list([TIMING_9, TIMING_10, TIMING_12])
        self.base_fields['minute_per_km_run_up_training_id'].choices = get_training_timing_description_list([TIMING_9, TIMING_10, TIMING_12])
        self.base_fields['minute_per_km_runway_id'].choices = get_training_timing_description_list([TIMING_11])
        self.base_fields['warmup_id'].choices = get_warmup_frequency_description_list()
        # self['running_training_type'].field.choices = running_training_types
