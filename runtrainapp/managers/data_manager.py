from runtrainapp.models import *
from ..utils.constants import *
from ..utils.form_constants import *
from dateutil import parser


def get_training_provider_by_name(provider_name):
    return TrainingProvider.objects.get(description__iexact=provider_name)


def get_training_type_by_id(type_id):
    return TrainingType.objects.get(id=type_id)


# Return training type by description or Type Other
def get_training_type_by_description(description):
    try:
        return TrainingType.objects.get(description=description)
    except TrainingType.DoesNotExist:
        return TrainingType.objects.get(id=TYPE_OTHER)


# Get training types list
# Running excluded by default
def get_training_types_description_list(exclude_running=True):
    if exclude_running:
        all_training_types = TrainingType.objects.exclude(id=TYPE_RUNNING)
    else:
        all_training_types = TrainingType.objects.all()

    result = []
    for training_type in all_training_types:
        result.append((training_type.description, training_type.description))

    return result


# Get user list
# Running excluded by default
def get_user_list(user_name, is_admin=False):
    if is_admin:
        user_list = User.objects.all()
    else:
        user_list = User.objects.filter(username=user_name)

    result = []
    for user in user_list:
        result.append((user.username, user.username))

    return result


def get_running_training_type_by_id(type_id):
    return RunningTrainingType.objects.get(id=type_id)


def get_trainings_amount_by_provider_and_user(provider, user):
    return Training.objects.filter(user=user, provider=provider).count()


def get_one_km_timing_by_description(description):
    return OneKmTiming.objects.get(description=description)


def get_five_km_timing_by_description(description):
    return FiveKmTiming.objects.get(description=description)


def get_ten_km_timing_by_description(description):
    return TenKmTiming.objects.get(description=description)


def get_half_marathon_timing_by_description(description):
    return HalfMarathonTiming.objects.get(description=description)


def get_marathon_timing_by_description(description):
    return MarathonTiming.objects.get(description=description)


def get_training_timing_by_description(description):
    return TrainingTiming.objects.get(description=description)


def get_wellness_type_by_description(description):
    return WellnessType.objects.get(description=description)


def get_warmup_frequency_by_description(description):
    return WarmupFrequency.objects.get(description=description)


def get_all_form_responses():
    return FormResponse.objects.all()


def get_all_form_responses_count():
    return FormResponse.objects.count()


# Create Training object and save into DB or return existing object
def create_training(user, provider, training_type, start_date, elapsed_time, external_code=None):
    obj, created = Training.objects.get_or_create(
        user=user,
        type=training_type,
        start_date=start_date,
        time=elapsed_time,
        provider=provider,
        defaults={
            'external_code': external_code,
        }
    )

    if created:
        print("Training created\t- User: %s\t Provider: %s\t External_code: %s" % (user.username, provider.description, external_code))
    else:
        print("Training exists\t- User: %s\t Provider: %s\t External_code: %s" % (user.username, provider.description, external_code))

    return obj


# Create Training object and save into DB or return existing object
def create_running_training(training, distance, avg_speed, running_training_type, segments=1):
    # This syntax checking only if Running Training for specific training is unique
    obj, created = RunningTraining.objects.get_or_create(
        training=training,
        defaults={
            'type': running_training_type,
            'distance': distance,
            'avg_speed': avg_speed,
            'segments_amount': segments
        }

    )

    if created:
        print("Running Training created\t- Training ID: %i\t Distance: %f\t Avg Speed: %f" % (training.id, distance, avg_speed))
    else:
        print("Running Training exists\t- Training ID: %i\t Distance: %f\t Avg Speed: %f" % (training.id, distance, avg_speed))

    return obj


# General method to create FormResponse and related ResponseOtherTraining and ResponseWellness
# data_dict is used to retrieve all parsed data
def create_form_response_and_related_data_by_dict(data_dict):
    form_response_obj = create_form_response_by_dict(data_dict)

    other_trainings_list = data_dict[INDEX_OTHER_TRAININGS_TYPES]
    create_response_other_trainings_from_list(other_trainings_list, form_response_obj)

    wellness_list = data_dict[INDEX_WELLNESS_TYPES]
    create_response_wellness_from_list(wellness_list, form_response_obj)


# Create ResponseWellness object and save into DB or return existing object
def create_form_response_by_dict(data_dict):
    obj, created = FormResponse.objects.get_or_create(
        year_of_birth=data_dict[INDEX_YEAR_OF_BIRTH],
        height=data_dict[INDEX_HEIGHT],
        weight=data_dict[INDEX_WEIGHT],
        running_years=data_dict[INDEX_RUNNING_YEARS],
        time_1km=data_dict[INDEX_TIME_1KM],
        time_5km=data_dict[INDEX_TIME_5KM],
        time_10km=data_dict[INDEX_TIME_10KM],
        time_21km=data_dict[INDEX_TIME_21KM],
        time_42km=data_dict[INDEX_TIME_42KM],
        training_amount=data_dict[INDEX_TRAINING_AMOUNT],
        km_amount=data_dict[INDEX_KM_AMOUNT],
        speed_training_amount=data_dict[INDEX_SPEED_TRAINING_AMOUNT],
        minute_per_km_speed_training=data_dict[INDEX_MINUTE_PER_KM_SPEED_TRAINING],
        threshold_training_amount=data_dict[INDEX_THRESHOLD_TRAINING_AMOUNT],
        minute_per_km_threshold_training=data_dict[INDEX_MINUTE_PER_KM_THRESHOLD_TRAINING],
        interval_training_amount=data_dict[INDEX_INTERVAL_TRAINING_AMOUNT],
        minute_per_km_interval_training=data_dict[INDEX_MINUTE_PER_KM_INTERVAL_TRAINING],
        run_up_training_amount=data_dict[INDEX_RUN_UP_TRAINING_AMOUNT],
        minute_per_km_run_up_training=data_dict[INDEX_MINUTE_PER_KM_RUN_UP_TRAINING],
        runway_amount=data_dict[INDEX_RUNWAY_AMOUNT],
        km_per_runway=data_dict[INDEX_KM_PER_RUNWAY],
        minute_per_km_runway=data_dict[INDEX_MINUTE_PER_KM_RUNWAY],
        other_trainings=data_dict[INDEX_OTHER_TRAININGS],
        other_trainings_amount=data_dict[INDEX_OTHER_TRAININGS_AMOUNT],
        other_trainings_time=data_dict[INDEX_OTHER_TRAININGS_TIME],
        wellness=data_dict[INDEX_WELLNESS],
        wellness_amount=data_dict[INDEX_WELLNESS_AMOUNT],
        detraining_amount=data_dict[INDEX_DETRAINING_AMOUNT],
        detraining_days=data_dict[INDEX_DETRAINING_DAYS],
        warmup=data_dict[INDEX_WARMUP],
        warmup_time=data_dict[INDEX_WARMUP_TIME]
    )

    if created:
        print("FormResponseID:  %s\t- CREATED" % obj.id)
    else:
        print("FormResponseID:  %s\t- EXIST" % obj.id)

    return obj


# Create ResponseOtherTraining objects related to FormResponse
def create_response_other_trainings_from_list(other_trainings_list, related_form_response):
    created_objects_list = []
    for other_training in other_trainings_list:
        obj = create_response_other_training(related_form_response, other_training)
        created_objects_list.append(obj)

    return created_objects_list


# Create ResponseOtherTraining object and save into DB or return existing object
def create_response_other_training(form_response, other_training):
    obj, created = ResponseOtherTraining.objects.get_or_create(
        response=form_response,
        other_training_type=other_training
    )

    if created:
        print("ResponseOtherTraining:  %s\t- CREATED" % obj.id)
    else:
        print("ResponseOtherTraining:  %s\t- EXIST" % obj.id)

    return obj


# Create ResponseWellness objects related to FormResponse
def create_response_wellness_from_list(wellness_type_list, related_form_response):
    created_objects_list = []
    for wellness_type in wellness_type_list:
        obj = create_response_wellness(related_form_response, wellness_type)
        created_objects_list.append(obj)

    return created_objects_list


# Create ResponseWellness object and save into DB or return existing object
def create_response_wellness(form_response, wellness_type):
    obj, created = ResponseWellness.objects.get_or_create(
        response=form_response,
        wellness_type=wellness_type
    )

    if created:
        print("ResponseWellness:  %s\t- CREATED" % obj.id)
    else:
        print("ResponseWellness:  %s\t- EXIST" % obj.id)

    return obj


# Parse POST request for training add
def parse_training_request(request):
    post_request = request.POST
    start_date = parse_date_time_from_string(post_request.get('start_date'))
    # Change training type to seconds (As data from strava)
    training_time = int(post_request.get('training_time')) * 60
    training_type = get_training_type_by_description(post_request.get('training_type'))
    # Get user from request or use current as default
    user = post_request.get('user', request.user)
    # Manual training provider
    training_provider = get_training_provider_by_name(TRAINING_PROVIDER_MANUAL)

    training = create_training(user, training_provider, training_type, start_date, training_time)

    return training


def parse_date_time_from_string(date_time_str):
    return parser.parse(date_time_str)
