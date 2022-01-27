from .form_constants import *
from ..managers.data_manager import *
from ..models import *


def parse_response_row(row):
    year_of_birth = parse_year_of_birth(row)
    print(year_of_birth)
    height = parse_height(row)
    print(height)
    weight = parse_weight(row)
    print(weight)
    running_years = parse_running_years(row)
    print(running_years)
    time_1km = parse_time_1km(row)
    print(time_1km)
    time_5km = parse_time_5km(row)
    print(time_5km)
    time_10km = parse_time_10km(row)
    print(time_10km)
    time_21km = parse_time_21km(row)
    print(time_21km)
    time_42km = parse_time_42km(row)
    print(time_42km)
    training_amount = parse_training_amount(row)
    print(training_amount)
    km_amount = parse_km_amount(row)
    print(km_amount)
    speed_training_amount = parse_speed_training_amount(row)
    print(speed_training_amount)
    minute_per_km_speed_training = parse_minute_per_km_speed_training(row)
    print(minute_per_km_speed_training)
    threshold_training_amount = parse_threshold_training_amount(row)
    print(threshold_training_amount)
    minute_per_km_threshold_training = parse_minute_per_km_threshold_training(row)
    print(minute_per_km_threshold_training)
    interval_training_amount = parse_interval_training_amount(row)
    print(interval_training_amount)
    minute_per_km_interval_training = parse_minute_per_km_interval_training(row)
    print(minute_per_km_interval_training)
    run_up_training_amount = parse_run_up_training_amount(row)
    print(run_up_training_amount)
    minute_per_km_run_up_training = parse_minute_per_km_run_up_training(row)
    print(minute_per_km_run_up_training)
    runway_amount = parse_runway_amount(row)
    print(runway_amount)
    km_per_runway = parse_km_per_runway(row)
    print(km_per_runway)
    minute_per_km_runway = parse_minute_per_km_runway(row)
    print(minute_per_km_runway)
    other_trainings = parse_other_trainings(row)
    print(other_trainings)
    other_trainings_types = parse_other_trainings_types_list_str(row)
    print(other_trainings_types)
    other_trainings_amount = parse_other_trainings_amount(row)
    print(other_trainings_amount)
    other_trainings_time = parse_other_trainings_time(row)
    print(other_trainings_time)
    wellness = parse_wellness(row)
    print(wellness)
    wellness_types = parse_wellness_types_list_str(row)
    print(wellness_types)
    wellness_amount = parse_wellness_amount(row)
    print(wellness_amount)
    detraining_amount = parse_detraining_amount(row)
    print(detraining_amount)
    detraining_days = parse_detraining_days(row)
    print(detraining_days)
    warmup = parse_warmup(row)
    print(warmup)
    warmup_time = parse_warmup_time(row)
    print(warmup_time)


# Parse year of birth from response
# Type Integer
def parse_year_of_birth(row):
    year_of_birth = row[INDEX_YEAR_OF_BIRTH]
    return year_of_birth


# Parse height from response
# Type Integer
def parse_height(row):
    height = row[INDEX_HEIGHT]
    return height


# Parse weight from response
# Type Integer
def parse_weight(row):
    weight = row[INDEX_WEIGHT]
    return weight


# Parse running_years from response
# Type Float
def parse_running_years(row):
    running_years = row[INDEX_RUNNING_YEARS]
    return running_years


# Parse time_1km from response
# Type Str
# Return OneKmTiming
def parse_time_1km(row):
    time_1km = row[INDEX_TIME_1KM]
    time_1km_obj = get_one_km_timing_by_description(time_1km)
    return time_1km_obj


# Parse time_5km from response
# Type Str
# Return FiveKmTiming
def parse_time_5km(row):
    time_5km = row[INDEX_TIME_5KM]
    time_5km_obj = get_five_km_timing_by_description(time_5km)
    return time_5km_obj


# Parse time_10km from response
# Type Str
# Return TenKmTiming
def parse_time_10km(row):
    time_10km = row[INDEX_TIME_10KM]
    time_10km_obj = get_ten_km_timing_by_description(time_10km)
    return time_10km_obj


# Parse time_21km from response
# Type Str
# Return HalfMarathonTiming
def parse_time_21km(row):
    time_21km = row[INDEX_TIME_21KM]
    time_21km_obj = get_half_marathon_timing_by_description(time_21km)
    return time_21km_obj


# Parse time_42km from response
# Type Str
# Return MarathonTiming
def parse_time_42km(row):
    time_42km = row[INDEX_TIME_42KM]
    time_42km_obj = get_marathon_timing_by_description(time_42km)
    return time_42km_obj


# Parse training_amount from response
# Type Int
def parse_training_amount(row):
    training_amount = row[INDEX_TRAINING_AMOUNT]
    return training_amount


# Parse km_amount from response
# Type Int
def parse_km_amount(row):
    km_amount = row[INDEX_KM_AMOUNT]
    return km_amount


# Parse speed_training_amount from response
# Type Int
def parse_speed_training_amount(row):
    speed_training_amount = row[INDEX_SPEED_TRAINING_AMOUNT]
    return speed_training_amount


# Parse minute_per_km_speed_training from response
# Type Str
# Return TrainingTiming
def parse_minute_per_km_speed_training(row):
    minute_per_km_speed_training = row[INDEX_MINUTE_PER_KM_SPEED_TRAINING]
    minute_per_km_speed_training_obj = get_training_timing_by_description(minute_per_km_speed_training)
    return minute_per_km_speed_training_obj


# Parse threshold_training_amount from response
# Type Int
def parse_threshold_training_amount(row):
    threshold_training_amount = row[INDEX_THRESHOLD_TRAINING_AMOUNT]
    return threshold_training_amount


# Parse minute_per_km_threshold_training from response
# Type Str
# Return TrainingTiming
def parse_minute_per_km_threshold_training(row):
    minute_per_km_threshold_training = row[INDEX_MINUTE_PER_KM_THRESHOLD_TRAINING]
    minute_per_km_threshold_training_obj = get_training_timing_by_description(minute_per_km_threshold_training)
    return minute_per_km_threshold_training_obj


# Parse interval_training_amount from response
# Type Int
def parse_interval_training_amount(row):
    interval_training_amount = row[INDEX_INTERVAL_TRAINING_AMOUNT]
    return interval_training_amount


# Parse minute_per_km_interval_training from response
# Type Str
# Return TrainingTiming
def parse_minute_per_km_interval_training(row):
    minute_per_km_interval_training = row[INDEX_MINUTE_PER_KM_INTERVAL_TRAINING]
    minute_per_km_interval_training_obj = get_training_timing_by_description(minute_per_km_interval_training)
    return minute_per_km_interval_training_obj


# Parse run_up_training_amount from response
# Type Int
def parse_run_up_training_amount(row):
    run_up_training_amount = row[INDEX_RUN_UP_TRAINING_AMOUNT]
    return run_up_training_amount


# Parse minute_per_km_run_up_training from response
# Type Str
# Return TrainingTiming
def parse_minute_per_km_run_up_training(row):
    minute_per_km_run_up_training = row[INDEX_MINUTE_PER_KM_RUN_UP_TRAINING]
    minute_per_km_run_up_training_obj = get_training_timing_by_description(minute_per_km_run_up_training)
    return minute_per_km_run_up_training_obj


# Parse runway_amount from response
# Type Int
def parse_runway_amount(row):
    runway_amount = row[INDEX_RUNWAY_AMOUNT]
    return runway_amount


# Parse km_per_runway from response
# Type Int
def parse_km_per_runway(row):
    km_per_runway = row[INDEX_KM_PER_RUNWAY]
    return km_per_runway


# Parse minute_per_km_runway from response
# Type Str
# Return TrainingTiming
def parse_minute_per_km_runway(row):
    minute_per_km_runway = row[INDEX_MINUTE_PER_KM_RUNWAY]
    minute_per_km_runway_obj = get_training_timing_by_description(minute_per_km_runway)
    return minute_per_km_runway_obj


# Parse other_trainings from response
# Type Str
def parse_other_trainings(row):
    other_trainings = row[INDEX_OTHER_TRAININGS]
    other_trainings_boolean = parse_boolean_str(other_trainings)
    return other_trainings_boolean


# Parse other_trainings_types_list from response
# Type String
# Return List TrainingTypes
def parse_other_trainings_types_list_str(row):
    other_trainings_types_obj_list = []
    other_trainings_types_list_str = row[INDEX_OTHER_TRAININGS_TYPES]
    if other_trainings_types_list_str is not None:
        other_trainings_types_list = other_trainings_types_list_str.split(LIST_SEPARATOR)

        for other_training_type in other_trainings_types_list:
            other_training_type_obj = parse_other_training_type(other_training_type)
            other_trainings_types_obj_list.append(other_training_type_obj)

    return other_trainings_types_obj_list


# Parse other_trainings_types_list from other_trainings_types_list
# Type String
# Return TrainingType
def parse_other_training_type(other_training_type_str):
    other_training_type_obj = get_training_type_by_description(other_training_type_str)
    return other_training_type_obj


# Parse other_trainings_amount from response
# Type Float
def parse_other_trainings_amount(row):
    other_trainings_amount = row[INDEX_OTHER_TRAININGS_AMOUNT]
    return other_trainings_amount


# Parse other_trainings_time from response
# Type Float
def parse_other_trainings_time(row):
    other_trainings_time = row[INDEX_OTHER_TRAININGS_TIME]
    return other_trainings_time


# Parse wellness from response
# Type Str
def parse_wellness(row):
    wellness = row[INDEX_WELLNESS]
    wellness_boolean = parse_boolean_str(wellness)
    return wellness_boolean


# Parse wellness_types from response
# Type Str - Example: 'Rozciąganie/Joga;Rolowanie'
def parse_wellness_types_list_str(row):
    wellness_types_obj_list = []
    wellness_types_list_str = row[INDEX_WELLNESS_TYPES]
    if wellness_types_list_str is not None:
        wellness_types_list = wellness_types_list_str.split(LIST_SEPARATOR)

        for wellness_type in wellness_types_list:
            wellness_type_obj = parse_wellness_type(wellness_type)
            wellness_types_obj_list.append(wellness_type_obj)

    return wellness_types_obj_list


# Parse wellness_type_str from wellness_types_list
# Type String
# Return WellnessType
def parse_wellness_type(wellness_type_str):
    wellness_type_obj = get_wellness_type_by_description(wellness_type_str)
    return wellness_type_obj


# Parse wellness_amount from response
# Type Float
def parse_wellness_amount(row):
    wellness_amount = row[INDEX_WELLNESS_AMOUNT]
    return wellness_amount


# Parse detraining_amount from response
# Type Int
def parse_detraining_amount(row):
    detraining_amount = row[INDEX_DETRAINING_AMOUNT]
    return detraining_amount


# Parse detraining_days from response
# Type Int
def parse_detraining_days(row):
    detraining_days = row[INDEX_DETRAINING_DAYS]
    return detraining_days


# Parse warmup from response
# Type Str
# Return WarmupFrequency
def parse_warmup(row):
    warmup = row[INDEX_WARMUP]
    warmup_obj = get_warmup_frequency_by_description(warmup)
    return warmup_obj


# Parse warmup_time from response
# Type Int
def parse_warmup_time(row):
    warmup_time = row[INDEX_WARMUP_TIME]
    return warmup_time


# Parse str value to True/False basing on constant str
def parse_boolean_str(boolean_str):
    if boolean_str.lower() == STR_TRUE:
        return True
    else:
        return False
