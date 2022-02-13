import requests
from http import HTTPStatus
from dateutil import parser
from .auth_manager import *
from .data_manager import *
from .exception_manager import *


def get_list_of_running_activities(user):
    token = get_active_token_from_user(user, STRAVA_ACCOUNT_PROVIDER)
    activities_json_list = get_all_activities_from_strava_as_json_list(user, token)
    if activities_json_list is None:
        return None

    filtered_json_list = list(filter(lambda x: (x.get('type') == 'Run'), activities_json_list))

    if is_creation_needed(filtered_json_list, user, STRAVA_ACCOUNT_PROVIDER):
        create_running_trainings(filtered_json_list, user, STRAVA_ACCOUNT_PROVIDER)

    return filtered_json_list


# Invoke Strava API to get all activities from a user
# param per_page - amount of activities per call
# param page - page number
def get_all_activities_from_strava_as_json_list(user, token):
    if token is None:
        return None

    all_activities = []
    continue_execution = True
    page = 1

    while continue_execution:
        response = requests.get(LIST_ACTIVITIES_URL,
                                headers={
                                    'Authorization': 'Bearer ' + token
                                },
                                params={
                                    'page': page,
                                    'per_page': PER_PAGE
                                })

        check_api_response(response, user)

        json_list = response.json()

        # If call will return empty list - finish execution
        if json_list:
            all_activities.extend(json_list)
            page += 1
        else:
            continue_execution = False

    return all_activities


# Parse data from activity, create trainings and create running trainings
def create_running_trainings(activities_json_list, user, provider_name):
    training_type_running = get_training_type_by_id(TYPE_RUNNING)
    running_training_type_not_specified = get_running_training_type_by_id(RUNNING_TYPE_NOT_SPECIFIED)
    activities_json_list = create_trainings(activities_json_list, user, provider_name, training_type_running)

    for activity_json in activities_json_list:
        training_obj = activity_json['training_obj']
        distance = activity_json['distance']
        avg_speed = activity_json['average_speed']

        create_running_training(training_obj, distance, avg_speed, running_training_type_not_specified)


# Parse data from activity and create training
def create_trainings(activities_json_list, user, provider_name, training_type):
    provider_obj = get_training_provider_by_name(provider_name)

    for activity_json in activities_json_list:
        start_date = parser.parse(activity_json['start_date_local'])
        elapsed_time = activity_json['moving_time']
        external_code = activity_json['id']
        obj = create_training(user, provider_obj, training_type, start_date, elapsed_time, external_code)
        activity_json['training_obj'] = obj

    return activities_json_list


# Verify response status
def check_api_response(response, user):
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        raise_auth_exception(user)
    elif response.status_code != HTTPStatus.OK:
        raise_http_exception(response.status_code)


# Verify amount of existing activities
# Amount equals response activities amount - False else True
def is_creation_needed(activities_json_list, user, provider):
    provider_obj = get_training_provider_by_name(provider)
    existing_trainings_amount = get_trainings_amount_by_provider_and_user(provider_obj, user)
    return existing_trainings_amount != len(activities_json_list)





