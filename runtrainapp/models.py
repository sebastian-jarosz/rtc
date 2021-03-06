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
    external_code = models.CharField(max_length=100, null=True)

    def __str__(self):
        return "Trening - ID: %i\t- %s" % (self.id, self.type)

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
    # Prosz?? poda?? rok urodzenia
    year_of_birth = models.IntegerField()
    # Prosz?? poda?? sw??j wzrost (w centymetrach)
    height = models.IntegerField()
    # Prosz?? poda?? swoj?? wag?? (w kilogramach)
    weight = models.IntegerField()
    # Od ilu lat regularnie biegasz?
    running_years = models.IntegerField()
    # W jakim zakresie jest Tw??j najlepszy czas na 1km? (HH:MM:SS)
    time_1km = models.ForeignKey(OneKmTiming, on_delete=models.PROTECT, null=True)
    # W jakim zakresie jest Tw??j najlepszy czas na 5km? (HH:MM:SS)
    time_5km = models.ForeignKey(FiveKmTiming, on_delete=models.PROTECT, null=True)
    # W jakim zakresie jest Tw??j najlepszy czas na 10km? (HH:MM:SS)
    time_10km = models.ForeignKey(TenKmTiming, on_delete=models.PROTECT, null=True)
    # W jakim zakresie jest Tw??j najlepszy czas na 21,0975km - P????maraton? (HH:MM:SS)
    time_21km = models.ForeignKey(HalfMarathonTiming, on_delete=models.PROTECT, null=True)
    # W jakim zakresie jest Tw??j najlepszy czas na 42,195km - Maraton? (HH:MM:SS)
    time_42km = models.ForeignKey(MarathonTiming, on_delete=models.PROTECT, null=True)
    # Ile trening??w biegowych wykonujesz ??rednio w ci??gu tygodnia?
    training_amount = models.IntegerField()
    # Ile kilometr??w pokonujesz ??rednio podczas trening??w biegowych w ci??gu tygodnia?
    km_amount = models.IntegerField()
    # Ile razy w ci??gu miesi??ca wykonujesz trening szybko??ci?
    speed_training_amount = models.IntegerField()
    # W jakim zakresie tempa wykonujesz trening szybko??ci? (w minutach na kilometr)
    minute_per_km_speed_training = models.ForeignKey('TrainingTiming', related_name='minute_per_km_speed_training',
                                                     on_delete=models.PROTECT)
    # Ile razy w ci??gu miesi??ca wykonujesz trening progowy?
    threshold_training_amount = models.IntegerField()
    # W jakim zakresie tempa wykonujesz trening progowy? (w minutach na kilometr)
    minute_per_km_threshold_training = models.ForeignKey('TrainingTiming', related_name='minute_per_km_threshold_training',
                                                         on_delete=models.PROTECT)
    # Ile razy w ci??gu miesi??ca wykonujesz trening interwa??owy?
    interval_training_amount = models.IntegerField()
    # W jakim zakresie tempa wykonujesz trening interwa??owy? (w minutach na kilometr)
    minute_per_km_interval_training = models.ForeignKey('TrainingTiming', related_name='minute_per_km_interval_training',
                                                        on_delete=models.PROTECT)
    # Ile razy w ci??gu miesi??ca wykonujesz podbiegi?
    run_up_training_amount = models.IntegerField()
    # W jakim zakresie tempa wykonujesz podbiegi? (w minutach na kilometr)
    minute_per_km_run_up_training = models.ForeignKey('TrainingTiming', related_name='minute_per_km_run_up_training',
                                                      on_delete=models.PROTECT)
    # Ile razy w ci??gu miesi??ca wykonujesz wybieganie?
    runway_amount = models.IntegerField()
    # Jaka jest ??rednia ilo???? kilometr??w wykonywana podczas jednego wybiegania?
    km_per_runway = models.IntegerField()
    # W jakim zakresie tempa wykonujesz wybieganie? (w minutach na kilometr)
    minute_per_km_runway = models.ForeignKey('TrainingTiming', related_name='minute_per_km_runway',
                                             on_delete=models.PROTECT)
    # Czy wykonujesz treningi inne ni?? biegowe?
    other_trainings = models.BooleanField()
    # Jakie typy trening??w, poza biegowymi, wykonujesz?
    other_trainings_types = ""
    # Ile razy w ci??gu miesi??ca wykonujesz powy??sze treningi? (sumarycznie)
    other_trainings_amount = models.IntegerField()
    # Ile minut ??rednio trwa pojedynczy trening?
    other_trainings_time = models.IntegerField()
    # Czy wykonujesz aktywno??ci zwi??zane z odnow?? biologiczn???
    wellness = models.BooleanField()
    # Jakie aktywno??ci zwi??zane z odnow?? biologiczn?? wykonujesz?
    wellness_types = ""
    # Ile razy w ci??gu miesi??ca wykonujesz powy??sze aktywno??ci? (sumarycznie)
    wellness_amount = models.IntegerField()
    # Ile razy w ci??gu roku stosujesz roztrenowanie?
    detraining_amount = models.IntegerField()
    # Jaki jest Tw??j ??redni czas trwania roztrenowania? (w dniach)
    detraining_days = models.IntegerField()
    # Czy stosujesz rozgrzewk?? przed treningiem biegowym?
    warmup = models.ForeignKey(WarmupFrequency, on_delete=models.PROTECT)
    # Jaki jest ??redni czas trwania rozgrzewki? (w minutach)
    warmup_time = models.IntegerField()

    def __str__(self):
        return "Odpowied?? - ID: %i\t- Rok urodzenia: %i\t Wzrost: %i\t Waga: %i\t Lata do??wiadczenia w bieganiu: %i" % \
               (self.id, self.year_of_birth, self.height, self.weight, self.running_years)


class ResponseOtherTraining(models.Model):
    response = models.ForeignKey(FormResponse, on_delete=models.CASCADE)
    other_training_type = models.ForeignKey(TrainingType, on_delete=models.PROTECT)


class ResponseWellness(models.Model):
    response = models.ForeignKey(FormResponse, on_delete=models.CASCADE)
    wellness_type = models.ForeignKey(WellnessType, on_delete=models.PROTECT)


class FormUser(models.Model):
    # CASCADE - User deleted, training deleted
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    response = models.ForeignKey(FormResponse, on_delete=models.CASCADE)
    is_main = models.BooleanField()
