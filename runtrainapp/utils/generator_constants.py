# FormResponse model column names
COL_YEAR_OF_BIRTH = 'year_of_birth'
COL_HEIGHT = 'height'
COL_WEIGHT = 'weight'
COL_RUNNING_YEARS = 'running_years'
COL_TIME_1KM = 'time_1km_id'
COL_TIME_5KM = 'time_5km_id'
COL_TIME_10KM = 'time_10km_id'
COL_TIME_21KM = 'time_21km_id'
COL_TIME_42KM = 'time_42km_id'
COL_TRAINING_AMOUNT = 'training_amount'
COL_KM_AMOUNT = 'km_amount'
COL_SPEED_TRAINING_AMOUNT = 'speed_training_amount'
COL_MINUTE_PER_KM_SPEED_TRAINING = 'minute_per_km_speed_training_id'
COL_THRESHOLD_TRAINING_AMOUNT = 'threshold_training_amount'
COL_MINUTE_PER_KM_THRESHOLD_TRAINING = 'minute_per_km_threshold_training_id'
COL_INTERVAL_TRAINING_AMOUNT = 'interval_training_amount'
COL_MINUTE_PER_KM_INTERVAL_TRAINING = 'minute_per_km_interval_training_id'
COL_RUN_UP_TRAINING_AMOUNT = 'run_up_training_amount'
COL_MINUTE_PER_KM_RUN_UP_TRAINING = 'minute_per_km_run_up_training_id'
COL_RUNWAY_AMOUNT = 'runway_amount'
COL_KM_PER_RUNWAY = 'km_per_runway'
COL_MINUTE_PER_KM_RUNWAY = 'minute_per_km_runway_id'
COL_OTHER_TRAININGS = 'other_trainings'
COL_OTHER_TRAININGS_AMOUNT = 'other_trainings_amount'
COL_OTHER_TRAININGS_TIME = 'other_trainings_time'
COL_WELLNESS = 'wellness'
COL_WELLNESS_AMOUNT = 'wellness_amount'
COL_DETRAINING_AMOUNT = 'detraining_amount'
COL_DETRAINING_DAYS = 'detraining_days'
COL_WARMUP = 'warmup_id'
COL_WARMUP_TIME = 'warmup_time'

# Questions
Q_YEAR_OF_BIRTH = "Proszę podać rok urodzenia"
Q_HEIGHT = "Proszę podać swój wzrost (w centymetrach)"
Q_WEIGHT = "Proszę podać swoją wagę (w kilogramach)"
Q_RUNNING_YEARS = "Od ilu lat regularnie biegasz?"
Q_TIME_1KM = "W jakim zakresie jest Twój najlepszy czas na 1km? (HH:MM:SS)"
Q_TIME_5KM = "W jakim zakresie jest Twój najlepszy czas na 5km? (HH:MM:SS)"
Q_TIME_10KM = "W jakim zakresie jest Twój najlepszy czas na 10km? (HH:MM:SS)"
Q_TIME_21KM = "W jakim zakresie jest Twój najlepszy czas na 21,0975km - Półmaraton? (HH:MM:SS)"
Q_TIME_42KM = "W jakim zakresie jest Twój najlepszy czas na 42,195km - Maraton? (HH:MM:SS)"
Q_TRAINING_AMOUNT = "Ile treningów biegowych wykonujesz średnio w ciągu tygodnia?"
Q_KM_AMOUNT = "Ile kilometrów pokonujesz średnio podczas treningów biegowych w ciągu tygodnia?"
Q_SPEED_TRAINING_AMOUNT = "Ile razy w ciągu miesiąca wykonujesz trening szybkości?"
Q_MINUTE_PER_KM_SPEED_TRAINING = "W jakim zakresie tempa wykonujesz trening szybkości? (w minutach na kilometr)"
Q_THRESHOLD_TRAINING_AMOUNT = "Ile razy w ciągu miesiąca wykonujesz trening progowy?"
Q_MINUTE_PER_KM_THRESHOLD_TRAINING = "W jakim zakresie tempa wykonujesz trening progowy? (w minutach na kilometr)"
Q_INTERVAL_TRAINING_AMOUNT = "Ile razy w ciągu miesiąca wykonujesz trening interwałowy?"
Q_MINUTE_PER_KM_INTERVAL_TRAINING = "W jakim zakresie tempa wykonujesz trening interwałowy? (w minutach na kilometr)"
Q_RUN_UP_TRAINING_AMOUNT = "Ile razy w ciągu miesiąca wykonujesz podbiegi?"
Q_MINUTE_PER_KM_RUN_UP_TRAINING = "W jakim zakresie tempa wykonujesz podbiegi? (w minutach na kilometr)"
Q_RUNWAY_AMOUNT = "Ile razy w ciągu miesiąca wykonujesz wybieganie?"
Q_KM_PER_RUNWAY = "Jaka jest średnia ilość kilometrów wykonywana podczas jednego wybiegania?"
Q_MINUTE_PER_KM_RUNWAY = "W jakim zakresie tempa wykonujesz wybieganie? (w minutach na kilometr)"
Q_OTHER_TRAININGS = "Czy wykonujesz treningi inne niż biegowe?"
Q_OTHER_TRAININGS_TYPES = "Jakie typy treningów, poza biegowymi, wykonujesz?"
Q_OTHER_TRAININGS_AMOUNT = "Ile razy w ciągu miesiąca wykonujesz powyższe treningi? (sumarycznie)"
Q_OTHER_TRAININGS_TIME = "Ile minut średnio trwa pojedynczy trening?"
Q_WELLNESS = "Czy wykonujesz aktywności związane z odnową biologiczną?"
Q_WELLNESS_TYPES = "Jakie aktywności związane z odnową biologiczną wykonujesz?"
Q_WELLNESS_AMOUNT = "Ile razy w ciągu miesiąca wykonujesz powyższe aktywności? (sumarycznie)"
Q_DETRAINING_AMOUNT = "Ile razy w ciągu roku stosujesz roztrenowanie?"
Q_DETRAINING_DAYS = "Jaki jest Twój średni czas trwania roztrenowania? (w dniach)"
Q_WARMUP = "Czy stosujesz rozgrzewkę przed treningiem biegowym?"
Q_WARMUP_TIME = "Jaki jest średni czas trwania rozgrzewki? (w minutach)"

# Generator input dict {column_name:question}
Q_GENERATOR_INPUT = {
    COL_TRAINING_AMOUNT: Q_TRAINING_AMOUNT,
    COL_KM_AMOUNT: Q_KM_AMOUNT,
    COL_SPEED_TRAINING_AMOUNT: Q_SPEED_TRAINING_AMOUNT,
    COL_MINUTE_PER_KM_SPEED_TRAINING: Q_MINUTE_PER_KM_SPEED_TRAINING,
    COL_THRESHOLD_TRAINING_AMOUNT: Q_THRESHOLD_TRAINING_AMOUNT,
    COL_MINUTE_PER_KM_THRESHOLD_TRAINING: Q_MINUTE_PER_KM_THRESHOLD_TRAINING,
    COL_INTERVAL_TRAINING_AMOUNT: Q_INTERVAL_TRAINING_AMOUNT,
    COL_MINUTE_PER_KM_INTERVAL_TRAINING: Q_MINUTE_PER_KM_INTERVAL_TRAINING,
    COL_RUN_UP_TRAINING_AMOUNT: Q_RUN_UP_TRAINING_AMOUNT,
    COL_MINUTE_PER_KM_RUN_UP_TRAINING: Q_MINUTE_PER_KM_RUN_UP_TRAINING,
    COL_RUNWAY_AMOUNT: Q_RUNWAY_AMOUNT,
    COL_KM_PER_RUNWAY: Q_KM_PER_RUNWAY,
    COL_MINUTE_PER_KM_RUNWAY: Q_MINUTE_PER_KM_RUNWAY,
    COL_OTHER_TRAININGS: Q_OTHER_TRAININGS,
    COL_OTHER_TRAININGS_AMOUNT: Q_OTHER_TRAININGS_AMOUNT,
    COL_OTHER_TRAININGS_TIME: Q_OTHER_TRAININGS_TIME,
    COL_WELLNESS: Q_WELLNESS,
    COL_WELLNESS_AMOUNT: Q_WELLNESS_AMOUNT,
    COL_DETRAINING_AMOUNT: Q_DETRAINING_AMOUNT,
    COL_DETRAINING_DAYS: Q_DETRAINING_DAYS,
    COL_WARMUP: Q_WARMUP,
    COL_WARMUP_TIME: Q_WARMUP_TIME
}
