import json

from .form_responses_manager import *
from .learn_manager import *
from ..models import *
from django.core import serializers


def generate_predictions(main_form_user):
    generate_predictions_by_form_user(main_form_user)
    improve_and_predict_by_main_form(main_form_user, improve_level=0.1)
    improve_and_predict_by_main_form(main_form_user, improve_level=0.2)


# Generate predictions basing on FormUser object
def generate_predictions_by_form_user(form_user):
    # Get form object
    form_response = FormResponse.objects.filter(id=form_user.response.id)

    # Prepare df from form object
    df = create_df_from_form_responses_obj_list(list(form_response.values()))

    # Prepare distance specific dfs
    df_time_1km, df_time_5km, df_time_10km, df_time_21km, df_time_42km = prepare_distance_dfs(df)

    X_time_1km, y_time_1km = split_X_y_by_distance_column(df_time_1km, COLUMN_TIME_1KM_ID)
    X_time_5km, y_time_5km = split_X_y_by_distance_column(df_time_5km, COLUMN_TIME_5KM_ID)
    X_time_10km, y_time_10km = split_X_y_by_distance_column(df_time_10km, COLUMN_TIME_10KM_ID)
    X_time_21km, y_time_21km = split_X_y_by_distance_column(df_time_21km, COLUMN_TIME_21KM_ID)
    X_time_42km, y_time_42km = split_X_y_by_distance_column(df_time_42km, COLUMN_TIME_42KM_ID)

    # Get models from file
    lr_model_1km = get_model_from_file(LR_MODEL_1KM)
    lr_model_5km = get_model_from_file(LR_MODEL_5KM)
    lr_model_10km = get_model_from_file(LR_MODEL_10KM)
    lr_model_21km = get_model_from_file(LR_MODEL_21KM)
    lr_model_42km = get_model_from_file(LR_MODEL_42KM)

    # Predictions
    lr_model_1km_pred = round_prediction(lr_model_1km.predict(X_time_1km))
    lr_model_5km_pred = round_prediction(lr_model_5km.predict(X_time_5km))
    lr_model_10km_pred = round_prediction(lr_model_10km.predict(X_time_10km))
    lr_model_21km_pred = round_prediction(lr_model_21km.predict(X_time_21km))
    lr_model_42km_pred = round_prediction(lr_model_42km.predict(X_time_42km))

    # Save predicted values
    save_predictions_on_form(form_user.response, lr_model_1km_pred,
                             lr_model_5km_pred, lr_model_10km_pred,
                             lr_model_21km_pred, lr_model_42km_pred)

    return form_user


# Get int (ID) from prediction
def round_prediction(prediction):
    # Flat array of arrays (result of predict)
    prediction = prediction.flatten()
    # Predictions cannot be float - rounding and casting to float
    prediction = np.around(prediction)
    prediction = prediction.astype(int)

    # Only one record expected
    return prediction[0]


# Improve current level of trainings and predict posible result
# decimal (percent) example 0.1, 0.2 - default percent 0.1
def improve_and_predict_by_main_form(user_main_form, improve_level=0.1):
    # Main response is a base for next predictions
    main_form_id = user_main_form.response.id
    improved_form = user_main_form.response

    # remove pk (copy instance) - https://docs.djangoproject.com/en/4.0/topics/db/queries/#copying-model-instances
    improved_form.pk = None

    clear_distance_timing_on_form(improved_form)

    # First improved form (by 10%)
    improved_form = improve_form_by_decimal(improved_form, improve_level)

    improved_form.save()

    form_user, crt = FormUser.objects.update_or_create(
        user=user_main_form.user,
        is_main=False,
        response=improved_form,
    )

    form_user = generate_predictions_by_form_user(form_user)

    # Fix overriden data
    user_main_form.response = FormResponse.objects.get(id=main_form_id)
    return form_user


# Get timing objects (per distance and prediction)
def save_predictions_on_form(form, model_1km_pred, model_5km_pred, model_10km_pred, model_21km_pred, model_42km_pred):
    one_km_timing = get_timing_by_model_and_id(OneKmTiming, model_1km_pred)
    five_km_timing = get_timing_by_model_and_id(FiveKmTiming, model_5km_pred)
    ten_km_timing = get_timing_by_model_and_id(TenKmTiming, model_10km_pred)
    half_marathon_timing = get_timing_by_model_and_id(HalfMarathonTiming, model_21km_pred)
    marathon_timing = get_timing_by_model_and_id(MarathonTiming, model_42km_pred)

    form.time_1km = one_km_timing
    form.time_5km = five_km_timing
    form.time_10km = ten_km_timing
    form.time_21km = half_marathon_timing
    form.time_42km = marathon_timing

    form.save()
    print("Form ID: %i\t - Updated" % form.id)


# Clear timing data before prediction
def clear_distance_timing_on_form(form):

    form.time_1km = None
    form.time_5km = None
    form.time_10km = None
    form.time_21km = None
    form.time_42km = None

    return form


# Improve FormResponse answers by decimal (percent) example 0.1, 0.2
# default percent 0.1
def improve_form_by_decimal(form, decimal=0.1):
    # By default 110%
    improve_decimal = 1 + decimal
    # Level used for choice fields or for 0 values
    improve_level = round(decimal * 10)

    print('training_amount')
    if form.training_amount > 0:
        form.training_amount = round(form.training_amount * improve_decimal)
    else:
        form.training_amount = improve_level

    print('km_amount')
    if form.km_amount > 0:
        form.km_amount = round(form.km_amount * improve_decimal)
    else:
        form.km_amount = improve_level

    print('speed_training_amount')
    if form.speed_training_amount > 0:
        form.speed_training_amount = round(form.speed_training_amount * improve_decimal)
    else:
        form.speed_training_amount = improve_level

    print('minute_per_km_speed_training')
    form.minute_per_km_speed_training = get_decreased_instance_by_level(form.minute_per_km_speed_training, improve_level, include_last=False, excluded_ids=[TIMING_9, TIMING_10, TIMING_12])

    print('threshold_training_amount')
    if form.threshold_training_amount > 0:
        form.threshold_training_amount = round(form.threshold_training_amount * improve_decimal)
    else:
        form.threshold_training_amount = improve_level
        
    print('minute_per_km_threshold_training')
    form.minute_per_km_threshold_training = get_decreased_instance_by_level(form.minute_per_km_threshold_training, improve_level, include_last=False, excluded_ids=[TIMING_9, TIMING_10, TIMING_12])

    print('interval_training_amount')
    if form.interval_training_amount > 0:
        form.interval_training_amount = round(form.interval_training_amount * improve_decimal)
    else:
        form.interval_training_amount = improve_level
        
    print('minute_per_km_interval_training')
    form.minute_per_km_interval_training = get_decreased_instance_by_level(form.minute_per_km_interval_training, improve_level, include_last=False, excluded_ids=[TIMING_9, TIMING_10, TIMING_12])

    print('run_up_training_amount')
    if form.run_up_training_amount > 0:
        form.run_up_training_amount = round(form.run_up_training_amount * improve_decimal)
    else:
        form.run_up_training_amount = improve_level

    print('minute_per_km_run_up_training')
    form.minute_per_km_run_up_training = get_decreased_instance_by_level(form.minute_per_km_run_up_training, improve_level, include_last=False, excluded_ids=[TIMING_9, TIMING_10, TIMING_12])

    print('runway_amount')
    if form.run_up_training_amount > 0:
        form.run_up_training_amount = round(form.run_up_training_amount * improve_decimal)
    else:
        form.run_up_training_amount = improve_level

    print('km_per_runway')
    if form.km_per_runway > 0:
        form.km_per_runway = round(form.km_per_runway * improve_decimal)
    else:
        form.km_per_runway = improve_level

    print('minute_per_km_runway')
    form.minute_per_km_runway = get_decreased_instance_by_level(form.minute_per_km_runway, improve_level, include_last=False, excluded_ids=[TIMING_11])

    print('other_trainings')
    print('SHOULD BE SAME')

    print('other_trainings_amount')
    if form.other_trainings_amount > 0:
        form.other_trainings_amount = round(form.other_trainings_amount * improve_decimal)
    # Change zero value only in case other_trainings true
    elif form.other_trainings:
        form.other_trainings_amount = improve_level

    print('other_trainings_time')
    if form.other_trainings_time > 0:
        form.other_trainings_time = round(form.other_trainings_time * improve_decimal)
    # Change zero value only in case other_trainings true
    elif form.other_trainings:
        form.other_trainings_time = improve_level

    print('wellness')
    print('SHOULD BE SAME')

    print('wellness_amount')
    if form.wellness_amount > 0:
        form.wellness_amount = round(form.wellness_amount * improve_decimal)
    # Change zero value only in case wellness true
    elif form.wellness:
        form.wellness_amount = improve_level

    print('detraining_amount')
    if form.detraining_amount > 0:
        form.detraining_amount = round(form.detraining_amount * improve_decimal)
    else:
        form.detraining_amount = improve_level

    print('detraining_days')
    if form.detraining_days > 0:
        form.detraining_days = round(form.detraining_days * improve_decimal)
    else:
        form.detraining_days = improve_level

    print('warmup')
    form.warmup = get_increased_instance_by_level(form.warmup, improve_level, include_last=False)

    print('warmup_time')
    if form.warmup_time > 0:
        form.warmup_time = round(form.warmup_time * improve_decimal)
    else:
        form.warmup_time = improve_level

    return form


def get_decreased_instance_by_level(model_record, improve_level, include_last=True, excluded_ids=[]):
    # Get model class
    model = type(model_record)
    model_min_id = 1
    model_max_id = model.objects.latest('id').id
    # Max record sometimes is not relevant
    if not include_last:
        model_max_id -= 1

    # Current record
    record_id = model_record.id
    new_id = record_id - improve_level

    while new_id in excluded_ids:
        new_id = new_id - improve_level

    if new_id < model_min_id:
        new_id = model_min_id

    decreased_record = model.objects.get(id=new_id)

    return decreased_record


def get_increased_instance_by_level(model_record, improve_level, include_last=True):
    # Get model class
    model = type(model_record)
    model_max_id = model.objects.latest('id').id
    # Max record sometimes is not relevant
    if not include_last:
        model_max_id -= 1

    # Current record
    record_id = model_record.id
    new_id = record_id + improve_level

    if new_id > model_max_id:
        new_id = model_max_id

    increased_record = model.objects.get(id=new_id)

    return increased_record
