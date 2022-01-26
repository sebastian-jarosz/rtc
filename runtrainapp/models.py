import datetime
from decimal import Decimal

from django.db import models
from django.contrib.auth.models import User


class TrainingProvider(models.Model):
    description = models.CharField(max_length=50)
    
    def __str__(self):
        return self.description


class RunningTrainingType(models.Model):
    description = models.CharField(max_length=50)
    detailed_description = models.CharField(max_length=500)

    def __str__(self):
        return self.description


class TrainingType(models.Model):
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.description


class WellnessType(models.Model):
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.description


class WarmupFrequency(models.Model):
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.description


class OneKmTiming(models.Model):
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description


class FiveKmTiming(models.Model):
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description


class TenKmTiming(models.Model):
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description


class HalfMarathonTiming(models.Model):
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description


class MarathonTiming(models.Model):
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description


class TrainingTiming(models.Model):
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description


class Training(models.Model):
    # CASCADE - User deleted, training deleted
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # PROTECT - Protects Training Type removal
    type = models.ForeignKey(TrainingType, on_delete=models.PROTECT)
    start_date = models.DateTimeField()
    # time in seconds
    time = models.IntegerField()
    # PROTECT - Protects Provider removal
    provider = models.ForeignKey(TrainingProvider, on_delete=models.PROTECT)
    # Training Code from Provider (if not Manual)
    external_code = models.CharField(max_length=100)

    def __str__(self):
        return "Training %i - %s" % (self.id, self.type)

    def get_formatted_time(self):
        return datetime.timedelta(seconds=self.time)

    def get_formatted_start_date(self):
        return self.start_date.strftime("%d/%m/%Y, %H:%M:%S")


class RunningTraining(models.Model):
    # OneToOneField - better to use in case of uniqueness
    training = models.OneToOneField(Training, on_delete=models.CASCADE)
    # PROTECT - Protects Running Training Type removal, can be null
    type = models.ForeignKey(RunningTrainingType, null=True, on_delete=models.PROTECT)
    # distance in meters
    distance = models.DecimalField(max_digits=10, decimal_places=2)
    # avg_speed in m/s
    avg_speed = models.DecimalField(max_digits=10, decimal_places=2)
    segments_amount = models.IntegerField()

    def get_distance_km(self):
        return round(self.distance/1000, 3)

    # m/s to km/h - 1m/s = 3,6 km/h
    def get_avg_speed_km_per_h(self):
        return round(self.avg_speed * Decimal(3.6), 3)


class FormResponse(models.Model):
    # Proszę podać rok urodzenia
    year_of_birth = models.IntegerField()
    # Proszę podać swój wzrost (w centymetrach)
    height = models.IntegerField()
    # Proszę podać swoją wagę (w kilogramach)
    weight = models.IntegerField()
    # Od ilu lat regularnie biegasz?
    running_years = models.IntegerField()
    # W jakim zakresie jest Twój najlepszy czas na 1km? (HH:MM:SS)
    time_1km = models.ForeignKey(OneKmTiming, on_delete=models.PROTECT)
    # W jakim zakresie jest Twój najlepszy czas na 5km? (HH:MM:SS)
    time_5km = models.ForeignKey(FiveKmTiming, on_delete=models.PROTECT)
    # W jakim zakresie jest Twój najlepszy czas na 10km? (HH:MM:SS)
    time_10km = models.ForeignKey(TenKmTiming, on_delete=models.PROTECT)
    # W jakim zakresie jest Twój najlepszy czas na 21,0975km - Półmaraton? (HH:MM:SS)
    time_21km = models.ForeignKey(HalfMarathonTiming, on_delete=models.PROTECT)
    # W jakim zakresie jest Twój najlepszy czas na 42,195km - Maraton? (HH:MM:SS)
    time_42km = models.ForeignKey(MarathonTiming, on_delete=models.PROTECT)
    # Ile treningów biegowych wykonujesz średnio w ciągu tygodnia?
    training_amount = models.IntegerField()
    # Ile kilometrów pokonujesz średnio podczas treningów biegowych w ciągu tygodnia?
    km_amount = models.IntegerField()
    # Ile razy w ciągu miesiąca wykonujesz trening szybkości?
    speed_training_amount = models.IntegerField()
    # W jakim zakresie tempa wykonujesz trening szybkości? (w minutach na kilometr)
    minute_per_km_speed_training = models.ForeignKey('TrainingTiming', related_name='minute_per_km_speed_training',
                                                     on_delete=models.PROTECT)
    # Ile razy w ciągu miesiąca wykonujesz trening progowy?
    threshold_training_amount = models.IntegerField()
    # W jakim zakresie tempa wykonujesz trening progowy? (w minutach na kilometr)
    minute_per_km_threshold_training = models.ForeignKey('TrainingTiming', related_name='minute_per_km_threshold_training',
                                                         on_delete=models.PROTECT)
    # Ile razy w ciągu miesiąca wykonujesz trening interwałowy?
    interval_training_amount = models.IntegerField()
    # W jakim zakresie tempa wykonujesz trening interwałowy? (w minutach na kilometr)
    minute_per_km_interval_training = models.ForeignKey('TrainingTiming', related_name='minute_per_km_interval_training',
                                                        on_delete=models.PROTECT)
    # Ile razy w ciągu miesiąca wykonujesz podbiegi?
    run_up_training_amount = models.IntegerField()
    # W jakim zakresie tempa wykonujesz podbiegi? (w minutach na kilometr)
    minute_per_km_run_up_training = models.ForeignKey('TrainingTiming', related_name='minute_per_km_run_up_training',
                                                      on_delete=models.PROTECT)
    # Ile razy w ciągu miesiąca wykonujesz wybieganie?
    runway_amount = models.IntegerField()
    # Jaka jest średnia ilość kilometrów wykonywana podczas jednego wybiegania?
    km_per_runway = models.IntegerField()
    # W jakim zakresie tempa wykonujesz wybieganie? (w minutach na kilometr)
    minute_per_km_runway = models.ForeignKey('TrainingTiming', related_name='minute_per_km_runway',
                                             on_delete=models.PROTECT)
    # Czy wykonujesz treningi inne niż biegowe?
    other_trainings = models.BooleanField()
    # Jakie typy treningów, poza biegowymi, wykonujesz?
    other_trainings_types = ""
    # Ile razy w ciągu miesiąca wykonujesz powyższe treningi? (sumarycznie)
    other_trainings_amount = models.IntegerField()
    # Ile minut średnio trwa pojedynczy trening?
    other_trainings_time = models.IntegerField()
    # Czy wykonujesz aktywności związane z odnową biologiczną?
    wellness = models.BooleanField()
    # Jakie aktywności związane z odnową biologiczną wykonujesz?
    wellness_types = ""
    # Ile razy w ciągu miesiąca wykonujesz powyższe aktywności? (sumarycznie)
    wellness_amount = models.IntegerField()
    # Ile razy w ciągu roku stosujesz roztrenowanie?
    detraining_amount = models.IntegerField()
    # Jaki jest Twój średni czas trwania roztrenowania? (w dniach)
    detraining_days = models.IntegerField()
    # Czy stosujesz rozgrzewkę przed treningiem biegowym?
    warmup = models.ForeignKey(WarmupFrequency, on_delete=models.PROTECT)
    # Jaki jest średni czas trwania rozgrzewki? (w minutach)
    warmup_time = models.IntegerField()


class ResponseOtherTraining(models.Model):
    response = models.ForeignKey(FormResponse, on_delete=models.CASCADE)
    other_training_type = models.ForeignKey(TrainingType, on_delete=models.PROTECT)


class ResponseWellness(models.Model):
    response = models.ForeignKey(FormResponse, on_delete=models.CASCADE)
    wellness_type = models.ForeignKey(WellnessType, on_delete=models.PROTECT)
