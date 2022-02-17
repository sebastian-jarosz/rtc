from allauth.account.forms import AddEmailForm
from allauth.account.models import EmailAddress
from runtrainapp.models import *
from django import forms
from runtrainapp.managers.data_manager import *
from datetime import datetime

from runtrainapp.utils.generator_constants import *


def get_current_date_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# Custom Form to block sending confirmation e-mail
class CustomAddEmailForm(AddEmailForm):
    def save(self, request):
        return EmailAddress.objects.add_email(
            request, self.user, self.cleaned_data["email"], confirm=False
        )


class AddTrainingForm(forms.Form):
    start_date = forms.DateTimeField(initial=get_current_date_time, label="Czas rozpoczęcia")
    training_time = forms.IntegerField(label='Długość treningu (w minutach)', min_value=1)
    training_type = forms.ChoiceField(label='Typ treningu')
    user = forms.ChoiceField(label='Użytkownik', disabled=True)

    def __init__(self, training_types, users, is_admin=False):
        super().__init__()
        self['training_type'].field.choices = training_types
        self['user'].field.choices = users

        # Enable field for admin
        if is_admin:
            self['user'].field.disabled = False


class ShowTrainingForm(forms.Form):
    id = forms.CharField(label="ID", disabled=True)
    user = forms.CharField(label='Użytkownik', disabled=True)
    type = forms.CharField(label='Typ treningu', disabled=True)
    start_date = forms.CharField(label="Czas rozpoczęcia", disabled=True)
    time = forms.CharField(label='Długość treningu (w minutach)', disabled=True)
    provider = forms.CharField(label='Sposób dodania', disabled=True)
    external_code = forms.CharField(label='Zewnętrzne ID', disabled=True)

    def __init__(self, training):
        super().__init__()
        self['id'].field.initial = training.id
        self['user'].field.initial = training.user
        self['type'].field.initial = training.type
        self['start_date'].field.initial = training.get_formatted_start_date()
        self['time'].field.initial = training.get_formatted_time()
        self['provider'].field.initial = training.provider
        self['external_code'].field.initial = training.external_code


class ShowFormResponse(forms.Form):
    year_of_birth = forms.CharField(label=Q_YEAR_OF_BIRTH, disabled=True)
    height = forms.CharField(label=Q_HEIGHT, disabled=True)
    weight = forms.CharField(label=Q_WEIGHT, disabled=True)
    running_years = forms.CharField(label=Q_RUNNING_YEARS, disabled=True)
    time_1km = forms.CharField(label=Q_TIME_1KM, disabled=True)
    time_5km = forms.CharField(label=Q_TIME_5KM, disabled=True)
    time_10km = forms.CharField(label=Q_TIME_10KM, disabled=True)
    time_21km = forms.CharField(label=Q_TIME_21KM, disabled=True)
    time_42km = forms.CharField(label=Q_TIME_42KM, disabled=True)
    training_amount = forms.CharField(label=Q_TRAINING_AMOUNT, disabled=True)
    km_amount = forms.CharField(label=Q_KM_AMOUNT, disabled=True)
    speed_training_amount = forms.CharField(label=Q_SPEED_TRAINING_AMOUNT, disabled=True)
    minute_per_km_speed_training_id = forms.CharField(label=Q_MINUTE_PER_KM_SPEED_TRAINING)
    threshold_training_amount = forms.CharField(label=Q_THRESHOLD_TRAINING_AMOUNT, disabled=True)
    minute_per_km_threshold_training_id = forms.CharField(label=Q_MINUTE_PER_KM_THRESHOLD_TRAINING)
    interval_training_amount = forms.CharField(label=Q_INTERVAL_TRAINING_AMOUNT, disabled=True)
    minute_per_km_interval_training_id = forms.CharField(label=Q_MINUTE_PER_KM_INTERVAL_TRAINING)
    run_up_training_amount = forms.CharField(label=Q_RUN_UP_TRAINING_AMOUNT, disabled=True)
    minute_per_km_run_up_training_id = forms.CharField(label=Q_MINUTE_PER_KM_RUN_UP_TRAINING)
    runway_amount = forms.CharField(label=Q_RUNWAY_AMOUNT, disabled=True)
    km_per_runway = forms.CharField(label=Q_KM_PER_RUNWAY, disabled=True)
    minute_per_km_runway_id = forms.CharField(label=Q_MINUTE_PER_KM_RUNWAY)
    other_trainings = forms.CharField(label=Q_OTHER_TRAININGS, disabled=True)
    other_trainings_amount = forms.CharField(label=Q_OTHER_TRAININGS_AMOUNT)
    other_trainings_time = forms.CharField(label=Q_OTHER_TRAININGS_TIME, disabled=True)
    wellness = forms.CharField(label=Q_WELLNESS, disabled=True)
    wellness_amount = forms.CharField(label=Q_WELLNESS_AMOUNT, disabled=True)
    detraining_amount = forms.CharField(label=Q_DETRAINING_AMOUNT, disabled=True)
    detraining_days = forms.CharField(label=Q_DETRAINING_DAYS, disabled=True)
    warmup_id = forms.CharField(label=Q_WARMUP)
    warmup_time = forms.CharField(label=Q_WARMUP_TIME, disabled=True)

    def __init__(self, response):
        super().__init__()
        self['year_of_birth'].field.initial = response.year_of_birth
        self['height'].field.initial = response.height
        self['weight'].field.initial = response.weight
        self['running_years'].field.initial = response.running_years
        self['time_1km'].field.initial = response.time_1km
        self['time_5km'].field.initial = response.time_5km
        self['time_10km'].field.initial = response.time_10km
        self['time_21km'].field.initial = response.time_21km
        self['time_42km'].field.initial = response.time_42km
        self['training_amount'].field.initial = response.training_amount
        self['km_amount'].field.initial = response.km_amount
        self['speed_training_amount'].field.initial = response.speed_training_amount
        self['minute_per_km_speed_training_id'].field.initial = response.minute_per_km_speed_training_id
        self['threshold_training_amount'].field.initial = response.threshold_training_amount
        self['minute_per_km_threshold_training_id'].field.initial = response.minute_per_km_threshold_training_id
        self['interval_training_amount'].field.initial = response.interval_training_amount
        self['minute_per_km_interval_training_id'].field.initial = response.minute_per_km_interval_training_id
        self['run_up_training_amount'].field.initial = response.run_up_training_amount
        self['minute_per_km_run_up_training_id'].field.initial = response.minute_per_km_run_up_training_id
        self['runway_amount'].field.initial = response.runway_amount
        self['km_per_runway'].field.initial = response.km_per_runway
        self['minute_per_km_runway_id'].field.initial = response.minute_per_km_runway_id
        self['other_trainings'].field.initial = response.other_trainings
        self['other_trainings_amount'].field.initial = response.other_trainings_amount
        self['other_trainings_time'].field.initial = response.other_trainings_time
        self['wellness'].field.initial = response.wellness
        self['wellness_amount'].field.initial = response.wellness_amount
        self['detraining_amount'].field.initial = response.detraining_amount
        self['detraining_days'].field.initial = response.detraining_days
        self['warmup_id'].field.initial = response.warmup_id
        self['warmup_time'].field.initial = response.warmup_time


class AddRunningTrainingForm(forms.Form):
    # Training part
    start_date = forms.DateTimeField(initial=get_current_date_time, label="Czas rozpoczęcia")
    training_time = forms.IntegerField(label='Długość treningu (w minutach)', min_value=1)
    user = forms.ChoiceField(label='Użytkownik', disabled=True)

    # Running Training part
    distance = forms.DecimalField(label='Dystans (w metrach)', min_value=0.1, decimal_places=2)
    # Segments - Default value 1
    segments_amount = forms.IntegerField(label='Ilość segmentów', initial=1, min_value=1)
    running_training_type = forms.ChoiceField(label='Typ treningu biegowego')

    def __init__(self, users, running_training_types, is_admin=False):
        super().__init__()
        self['user'].field.choices = users
        self['running_training_type'].field.choices = running_training_types

        # Enable field for admin
        if is_admin:
            self['user'].field.disabled = False


class GenerateTrainingForm(forms.Form):
    year_of_birth = forms.IntegerField(label=Q_YEAR_OF_BIRTH, min_value=1900, max_value=2022)
    height = forms.IntegerField(label=Q_HEIGHT, min_value=100, max_value=250)
    weight = forms.IntegerField(label=Q_WEIGHT, min_value=30, max_value=200)
    running_years = forms.IntegerField(label=Q_RUNNING_YEARS, min_value=0, max_value=50)
    training_amount = forms.IntegerField(label=Q_TRAINING_AMOUNT, min_value=0, max_value=50)
    km_amount = forms.IntegerField(label=Q_KM_AMOUNT, min_value=0, max_value=50)
    speed_training_amount = forms.IntegerField(label=Q_SPEED_TRAINING_AMOUNT, min_value=0, max_value=50)
    minute_per_km_speed_training_id = forms.ChoiceField(label=Q_MINUTE_PER_KM_SPEED_TRAINING)
    threshold_training_amount = forms.IntegerField(label=Q_THRESHOLD_TRAINING_AMOUNT, min_value=0, max_value=50)
    minute_per_km_threshold_training_id = forms.ChoiceField(label=Q_MINUTE_PER_KM_THRESHOLD_TRAINING)
    interval_training_amount = forms.IntegerField(label=Q_INTERVAL_TRAINING_AMOUNT, min_value=0, max_value=50)
    minute_per_km_interval_training_id = forms.ChoiceField(label=Q_MINUTE_PER_KM_INTERVAL_TRAINING)
    run_up_training_amount = forms.IntegerField(label=Q_RUN_UP_TRAINING_AMOUNT, min_value=0, max_value=50)
    minute_per_km_run_up_training_id = forms.ChoiceField(label=Q_MINUTE_PER_KM_RUN_UP_TRAINING)
    runway_amount = forms.IntegerField(label=Q_RUNWAY_AMOUNT, min_value=0, max_value=50)
    km_per_runway = forms.IntegerField(label=Q_KM_PER_RUNWAY, min_value=0, max_value=50)
    minute_per_km_runway_id = forms.ChoiceField(label=Q_MINUTE_PER_KM_RUNWAY)
    other_trainings = forms.BooleanField(label=Q_OTHER_TRAININGS, required=False)
    other_trainings_amount = forms.IntegerField(label=Q_OTHER_TRAININGS_AMOUNT)
    other_trainings_time = forms.IntegerField(label=Q_OTHER_TRAININGS_TIME, min_value=0, max_value=50)
    wellness = forms.BooleanField(label=Q_WELLNESS, required=False)
    wellness_amount = forms.IntegerField(label=Q_WELLNESS_AMOUNT, min_value=0, max_value=50)
    detraining_amount = forms.IntegerField(label=Q_DETRAINING_AMOUNT, min_value=0, max_value=50)
    detraining_days = forms.IntegerField(label=Q_DETRAINING_DAYS, min_value=0, max_value=50)
    warmup_id = forms.ChoiceField(label=Q_WARMUP)
    warmup_time = forms.IntegerField(label=Q_WARMUP_TIME, min_value=0, max_value=50)

    def __init__(self):
        super().__init__()
        self.base_fields['minute_per_km_speed_training_id'].choices = get_training_timing_description_list([TIMING_9, TIMING_10, TIMING_12])
        self.base_fields['minute_per_km_threshold_training_id'].choices = get_training_timing_description_list([TIMING_9, TIMING_10, TIMING_12])
        self.base_fields['minute_per_km_interval_training_id'].choices = get_training_timing_description_list([TIMING_9, TIMING_10, TIMING_12])
        self.base_fields['minute_per_km_run_up_training_id'].choices = get_training_timing_description_list([TIMING_9, TIMING_10, TIMING_12])
        self.base_fields['minute_per_km_runway_id'].choices = get_training_timing_description_list([TIMING_11])
        self.base_fields['warmup_id'].choices = get_warmup_frequency_description_list()
        # self['running_training_type'].field.choices = running_training_types
