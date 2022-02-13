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
    # Description needed for UI
    for training_type in all_training_types:
        result.append((training_type.description, training_type.description))

    return result


# Get running training types list
def get_running_training_types_description_list():
    all_running_training_types = RunningTrainingType.objects.all()

    result = []
    # Description needed for UI
    for training_type in all_running_training_types:
        result.append((training_type.description, training_type.description))

    return result


def get_user_by_username(username):
    return User.objects.get(username=username)

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


def get_running_training_type_by_description(description):
    try:
        return RunningTrainingType.objects.get(description=description)
    except RunningTrainingType.DoesNotExist:
        return RunningTrainingType.objects.get(id=RUNNING_TYPE_NOT_SPECIFIED)


def get_trainings_amount_by_provider_and_user(provider, user):
    return Training.objects.filter(user=user, provider=provider).count()


def get_one_km_timing_by_description(description):
    return OneKmTiming.objects.get(description=description)


# Get timing descriptions by model
def get_timing_description_list_by_model(model):
    all_timings = model.objects.all()

    result = []
    # Description needed for UI
    for timing in all_timings:
        result.append((timing.description, timing.description))

    return result


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


# Get timing descriptions by model
def get_training_timing_description_list(excluded_ids=[]):
    all_timings = TrainingTiming.objects.exclude(id__in=excluded_ids)

    result = []
    # Description needed for UI
    for timing in all_timings:
        result.append((timing.description, timing.description))

    return result


def get_wellness_type_by_description(description):
    return WellnessType.objects.get(description=description)


def get_warmup_frequency_by_description(description):
    return WarmupFrequency.objects.get(description=description)


# Get timing descriptions by model
def get_warmup_frequency_description_list():
    all_warmup_frequency = WarmupFrequency.objects.all()

    result = []
    # Description needed for UI
    for warmup_frequency in all_warmup_frequency:
        result.append((warmup_frequency.description, warmup_frequency.description))

    return result


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
def parse_training_request(request, is_running=False):
    post_request = request.POST
    # Training - start_date value
    start_date = parse_date_time_from_string(post_request.get('start_date'))
    # Training - time value - Change training_time to seconds (DB data consistency)
    training_time = int(post_request.get('training_time')) * 60
    # Training - type value
    if is_running:
        training_type = get_training_type_by_id(TYPE_RUNNING)
    else:
        training_type = get_training_type_by_description(post_request.get('training_type'))
    # Training - user - if no user in the request, use default (current)
    user = parse_user_from_request(request)
    # Training - provider value - Manual training provider
    training_provider = get_training_provider_by_name(TRAINING_PROVIDER_MANUAL)

    training = create_training(user, training_provider, training_type, start_date, training_time)

    return training


# Parse POST request for training add
def parse_running_training_request(request):
    training = parse_training_request(request, True)
    post_request = request.POST
    # Running Training - distance in meters value
    distance = int(post_request.get('distance'))
    # Running Training - avg_speed - meters per second (DB data consistency)
    avg_speed = round(distance/training.time, 3)
    # Running Training - segments value - Default 1
    segments_amount = int(post_request.get('segments_amount'))

    # Running Training - running training type value
    running_training_type = get_running_training_type_by_description(post_request.get('running_training_type'))

    running_training = create_running_training(training, distance, avg_speed, running_training_type, segments=segments_amount)

    return running_training


def parse_generate_training_request(request):
    post_request = request.POST
    # Generate Training - start_date value
    year_of_birth = int(post_request.get('year_of_birth'))
    height = int(post_request.get('height'))
    weight = int(post_request.get('weight'))
    running_years = int(post_request.get('running_years'))
    training_amount = int(post_request.get('training_amount'))
    km_amount = int(post_request.get('km_amount'))
    speed_training_amount = int(post_request.get('speed_training_amount'))
    minute_per_km_speed_training_id = get_training_timing_by_description(post_request.get('minute_per_km_speed_training_id'))
    threshold_training_amount = int(post_request.get('threshold_training_amount'))
    minute_per_km_threshold_training_id = get_training_timing_by_description(post_request.get('minute_per_km_threshold_training_id'))
    interval_training_amount = int(post_request.get('interval_training_amount'))
    minute_per_km_interval_training_id = get_training_timing_by_description(post_request.get('minute_per_km_interval_training_id'))
    run_up_training_amount = int(post_request.get('run_up_training_amount'))
    minute_per_km_run_up_training_id = get_training_timing_by_description(post_request.get('minute_per_km_interval_training_id'))
    runway_amount = int(post_request.get('runway_amount'))
    km_per_runway = int(post_request.get('km_per_runway'))
    minute_per_km_runway_id = get_training_timing_by_description(post_request.get('minute_per_km_runway_id'))
    # other_trainings - Default False
    other_trainings_str = post_request.get('other_trainings', 'false')
    if other_trainings_str.lower() == 'false':
        other_trainings = False
    else:
        other_trainings = True
    other_trainings_amount = int(post_request.get('other_trainings_amount'))
    other_trainings_time = int(post_request.get('other_trainings_time'))
    # wellness - Default False
    wellness_str = post_request.get('other_trainings', 'false')
    if wellness_str.lower() == 'false':
        wellness = False
    else:
        wellness = True
    wellness_amount = int(post_request.get('wellness_amount'))
    detraining_amount = int(post_request.get('detraining_amount'))
    detraining_days = int(post_request.get('detraining_days'))
    warmup_id = get_warmup_frequency_by_description(post_request.get('warmup_id'))
    warmup_time = int(post_request.get('warmup_time'))

    return 'training'


def parse_date_time_from_string(date_time_str):
    return parser.parse(date_time_str)


# Parse user by username
# or get default user (current)
def parse_user_from_request(request):
    username = request.POST.get('user')
    if username:
        user = get_user_by_username(username)
    else:
        user = request.user

    return user