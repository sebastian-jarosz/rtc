from .form_constants import *
from ..managers.data_manager import *
from ..models import *


def parse_response_row(row):
    # init empty dict in which data will be kept (basing on existing indexes for code reusage)
    parsed_data_dict = {}

    parse_year_of_birth(row, parsed_data_dict)
    parse_height(row, parsed_data_dict)
    parse_weight(row, parsed_data_dict)
    parse_running_years(row, parsed_data_dict)
    parse_time_1km(row, parsed_data_dict)
    parse_time_5km(row, parsed_data_dict)
    parse_time_10km(row, parsed_data_dict)
    parse_time_21km(row, parsed_data_dict)
    parse_time_42km(row, parsed_data_dict)
    parse_training_amount(row, parsed_data_dict)
    parse_km_amount(row, parsed_data_dict)
    parse_speed_training_amount(row, parsed_data_dict)
    parse_minute_per_km_speed_training(row, parsed_data_dict)
    parse_threshold_training_amount(row, parsed_data_dict)
    parse_minute_per_km_threshold_training(row, parsed_data_dict)
    parse_interval_training_amount(row, parsed_data_dict)
    parse_minute_per_km_interval_training(row, parsed_data_dict)
    parse_run_up_training_amount(row, parsed_data_dict)
    parse_minute_per_km_run_up_training(row, parsed_data_dict)
    parse_runway_amount(row, parsed_data_dict)
    parse_km_per_runway(row, parsed_data_dict)
    parse_minute_per_km_runway(row, parsed_data_dict)
    parse_other_trainings(row, parsed_data_dict)
    parse_other_trainings_types_list_str(row, parsed_data_dict)
    parse_other_trainings_amount(row, parsed_data_dict)
    parse_other_trainings_time(row, parsed_data_dict)
    parse_wellness(row, parsed_data_dict)
    parse_wellness_types_list_str(row, parsed_data_dict)
    parse_wellness_amount(row, parsed_data_dict)
    parse_detraining_amount(row, parsed_data_dict)
    parse_detraining_days(row, parsed_data_dict)
    parse_warmup(row, parsed_data_dict)
    parse_warmup_time(row, parsed_data_dict)

    return parsed_data_dict


# Parse year of birth from response
# Type Integer
def parse_year_of_birth(row, data_dict):
    year_of_birth = row[INDEX_YEAR_OF_BIRTH]
    data_dict[INDEX_YEAR_OF_BIRTH] = year_of_birth


# Parse height from response
# Type Integer
def parse_height(row, data_dict):
    height = row[INDEX_HEIGHT]
    data_dict[INDEX_HEIGHT] = height


# Parse weight from response
# Type Integer
def parse_weight(row, data_dict):
    weight = row[INDEX_WEIGHT]
    data_dict[INDEX_WEIGHT] = weight


# Parse running_years from response
# Type Float default 0
def parse_running_years(row, data_dict):
    running_years = row[INDEX_RUNNING_YEARS]
    data_dict[INDEX_RUNNING_YEARS] = running_years or 0


# Parse time_1km from response
# Type Str
# Return OneKmTiming
def parse_time_1km(row, data_dict):
    time_1km = row[INDEX_TIME_1KM]
    time_1km_obj = get_one_km_timing_by_description(time_1km)
    data_dict[INDEX_TIME_1KM] = time_1km_obj


# Parse time_5km from response
# Type Str
# Return FiveKmTiming
def parse_time_5km(row, data_dict):
    time_5km = row[INDEX_TIME_5KM]
    time_5km_obj = get_five_km_timing_by_description(time_5km)
    data_dict[INDEX_TIME_5KM] = time_5km_obj


# Parse time_10km from response
# Type Str
# Return TenKmTiming
def parse_time_10km(row, data_dict):
    time_10km = row[INDEX_TIME_10KM]
    time_10km_obj = get_ten_km_timing_by_description(time_10km)
    data_dict[INDEX_TIME_10KM] = time_10km_obj


# Parse time_21km from response
# Type Str
# Return HalfMarathonTiming
def parse_time_21km(row, data_dict):
    time_21km = row[INDEX_TIME_21KM]
    time_21km_obj = get_half_marathon_timing_by_description(time_21km)
    data_dict[INDEX_TIME_21KM] = time_21km_obj


# Parse time_42km from response
# Type Str
# Return MarathonTiming
def parse_time_42km(row, data_dict):
    time_42km = row[INDEX_TIME_42KM]
    time_42km_obj = get_marathon_timing_by_description(time_42km)
    data_dict[INDEX_TIME_42KM] = time_42km_obj


# Parse training_amount from response
# Type Int
def parse_training_amount(row, data_dict):
    training_amount = row[INDEX_TRAINING_AMOUNT]
    data_dict[INDEX_TRAINING_AMOUNT] = training_amount


# Parse km_amount from response
# Type Int
def parse_km_amount(row, data_dict):
    km_amount = row[INDEX_KM_AMOUNT]
    data_dict[INDEX_KM_AMOUNT] = km_amount


# Parse speed_training_amount from response
# Type Int
def parse_speed_training_amount(row, data_dict):
    speed_training_amount = row[INDEX_SPEED_TRAINING_AMOUNT]
    data_dict[INDEX_SPEED_TRAINING_AMOUNT] = speed_training_amount


# Parse minute_per_km_speed_training from response
# Type Str
# Return TrainingTiming
def parse_minute_per_km_speed_training(row, data_dict):
    minute_per_km_speed_training = row[INDEX_MINUTE_PER_KM_SPEED_TRAINING]
    minute_per_km_speed_training_obj = get_training_timing_by_description(minute_per_km_speed_training)
    data_dict[INDEX_MINUTE_PER_KM_SPEED_TRAINING] = minute_per_km_speed_training_obj


# Parse threshold_training_amount from response
# Type Int
def parse_threshold_training_amount(row, data_dict):
    threshold_training_amount = row[INDEX_THRESHOLD_TRAINING_AMOUNT]
    data_dict[INDEX_THRESHOLD_TRAINING_AMOUNT] = threshold_training_amount


# Parse minute_per_km_threshold_training from response
# Type Str
# Return TrainingTiming
def parse_minute_per_km_threshold_training(row, data_dict):
    minute_per_km_threshold_training = row[INDEX_MINUTE_PER_KM_THRESHOLD_TRAINING]
    minute_per_km_threshold_training_obj = get_training_timing_by_description(minute_per_km_threshold_training)
    data_dict[INDEX_MINUTE_PER_KM_THRESHOLD_TRAINING] = minute_per_km_threshold_training_obj


# Parse interval_training_amount from response
# Type Int
def parse_interval_training_amount(row, data_dict):
    interval_training_amount = row[INDEX_INTERVAL_TRAINING_AMOUNT]
    data_dict[INDEX_INTERVAL_TRAINING_AMOUNT] = interval_training_amount


# Parse minute_per_km_interval_training from response
# Type Str
# Return TrainingTiming
def parse_minute_per_km_interval_training(row, data_dict):
    minute_per_km_interval_training = row[INDEX_MINUTE_PER_KM_INTERVAL_TRAINING]
    minute_per_km_interval_training_obj = get_training_timing_by_description(minute_per_km_interval_training)
    data_dict[INDEX_MINUTE_PER_KM_INTERVAL_TRAINING] = minute_per_km_interval_training_obj


# Parse run_up_training_amount from response
# Type Int
def parse_run_up_training_amount(row, data_dict):
    run_up_training_amount = row[INDEX_RUN_UP_TRAINING_AMOUNT]
    data_dict[INDEX_RUN_UP_TRAINING_AMOUNT] = run_up_training_amount


# Parse minute_per_km_run_up_training from response
# Type Str
# Return TrainingTiming
def parse_minute_per_km_run_up_training(row, data_dict):
    minute_per_km_run_up_training = row[INDEX_MINUTE_PER_KM_RUN_UP_TRAINING]
    minute_per_km_run_up_training_obj = get_training_timing_by_description(minute_per_km_run_up_training)
    data_dict[INDEX_MINUTE_PER_KM_RUN_UP_TRAINING] = minute_per_km_run_up_training_obj


# Parse runway_amount from response
# Type Int
def parse_runway_amount(row, data_dict):
    runway_amount = row[INDEX_RUNWAY_AMOUNT]
    data_dict[INDEX_RUNWAY_AMOUNT] = runway_amount


# Parse km_per_runway from response
# Type Int
def parse_km_per_runway(row, data_dict):
    km_per_runway = row[INDEX_KM_PER_RUNWAY]
    data_dict[INDEX_KM_PER_RUNWAY] = km_per_runway


# Parse minute_per_km_runway from response
# Type Str
# Return TrainingTiming
def parse_minute_per_km_runway(row, data_dict):
    minute_per_km_runway = row[INDEX_MINUTE_PER_KM_RUNWAY]
    minute_per_km_runway_obj = get_training_timing_by_description(minute_per_km_runway)
    data_dict[INDEX_MINUTE_PER_KM_RUNWAY] = minute_per_km_runway_obj


# Parse other_trainings from response
# Type Str
def parse_other_trainings(row, data_dict):
    other_trainings = row[INDEX_OTHER_TRAININGS]
    other_trainings_boolean = parse_boolean_str(other_trainings)
    data_dict[INDEX_OTHER_TRAININGS] = other_trainings_boolean


# Parse other_trainings_types_list from response
# Type String
# Return List TrainingTypes
def parse_other_trainings_types_list_str(row, data_dict):
    other_trainings_types_obj_list = []
    other_trainings_types_list_str = row[INDEX_OTHER_TRAININGS_TYPES]
    if other_trainings_types_list_str is not None:
        other_trainings_types_list = other_trainings_types_list_str.split(LIST_SEPARATOR)

        for other_training_type in other_trainings_types_list:
            other_training_type_obj = parse_other_training_type(other_training_type)
            other_trainings_types_obj_list.append(other_training_type_obj)

    data_dict[INDEX_OTHER_TRAININGS_TYPES] = other_trainings_types_obj_list


# Parse other_trainings_types_list from other_trainings_types_list
# Type String
# Return TrainingType
def parse_other_training_type(other_training_type_str):
    other_training_type_obj = get_training_type_by_description(other_training_type_str)
    return other_training_type_obj


# Parse other_trainings_amount from response
# Type Float - Default 0
def parse_other_trainings_amount(row, data_dict):
    other_trainings_amount = row[INDEX_OTHER_TRAININGS_AMOUNT]
    data_dict[INDEX_OTHER_TRAININGS_AMOUNT] = other_trainings_amount or 0


# Parse other_trainings_time from response
# Type Float - Default 0
def parse_other_trainings_time(row, data_dict):
    other_trainings_time = row[INDEX_OTHER_TRAININGS_TIME]
    data_dict[INDEX_OTHER_TRAININGS_TIME] = other_trainings_time or 0


# Parse wellness from response
# Type Str
def parse_wellness(row, data_dict):
    wellness = row[INDEX_WELLNESS]
    wellness_boolean = parse_boolean_str(wellness)
    data_dict[INDEX_WELLNESS] = wellness_boolean


# Parse wellness_types from response
# Type Str - Example: 'Rozciąganie/Joga;Rolowanie'
def parse_wellness_types_list_str(row, data_dict):
    wellness_types_obj_list = []
    wellness_types_list_str = row[INDEX_WELLNESS_TYPES]
    if wellness_types_list_str is not None:
        wellness_types_list = wellness_types_list_str.split(LIST_SEPARATOR)

        for wellness_type in wellness_types_list:
            wellness_type_obj = parse_wellness_type(wellness_type)
            wellness_types_obj_list.append(wellness_type_obj)

    data_dict[INDEX_WELLNESS_TYPES] = wellness_types_obj_list


# Parse wellness_type_str from wellness_types_list
# Type String
# Return WellnessType
def parse_wellness_type(wellness_type_str):
    wellness_type_obj = get_wellness_type_by_description(wellness_type_str)
    return wellness_type_obj


# Parse wellness_amount from response
# Type Float - Default 0
def parse_wellness_amount(row, data_dict):
    wellness_amount = row[INDEX_WELLNESS_AMOUNT]
    data_dict[INDEX_WELLNESS_AMOUNT] = wellness_amount or 0


# Parse detraining_amount from response
# Type Int
def parse_detraining_amount(row, data_dict):
    detraining_amount = row[INDEX_DETRAINING_AMOUNT]
    data_dict[INDEX_DETRAINING_AMOUNT] = detraining_amount


# Parse detraining_days from response
# Type Int
def parse_detraining_days(row, data_dict):
    detraining_days = row[INDEX_DETRAINING_DAYS]
    data_dict[INDEX_DETRAINING_DAYS] = detraining_days


# Parse warmup from response
# Type Str
# Return WarmupFrequency
def parse_warmup(row, data_dict):
    warmup = row[INDEX_WARMUP]
    warmup_obj = get_warmup_frequency_by_description(warmup)
    data_dict[INDEX_WARMUP] = warmup_obj


# Parse warmup_time from response
# Type Int
def parse_warmup_time(row, data_dict):
    warmup_time = row[INDEX_WARMUP_TIME]
    data_dict[INDEX_WARMUP_TIME] = warmup_time


# Parse str value to True/False basing on constant str
def parse_boolean_str(boolean_str):
    if boolean_str.lower() == STR_TRUE:
        return True
    else:
        return False
