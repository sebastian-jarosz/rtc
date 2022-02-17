# List Athlete Activities (getLoggedInAthleteActivities)
# getLoggedInAthleteActivities URL
LIST_ACTIVITIES_URL = 'https://www.strava.com/api/v3/athlete/activities'

# refresh token URL Strava
REFRESH_TOKEN_STRAVA_URL = 'https://www.strava.com/oauth/token'

# Amount of activities returned in one call
PER_PAGE = 200

# Account Provider Name
STRAVA_ACCOUNT_PROVIDER = 'strava'

# Training Provider
TRAINING_PROVIDER_MANUAL = 'Manual'

# Training Type IDs
TYPE_STRENGTH = 1
TYPE_SWIMMING = 2
TYPE_CROSS = 3
TYPE_BIKE = 4
TYPE_PILATES = 5
TYPE_DANCE = 6
TYPE_MARTIAL_ARTS = 7
TYPE_RUNNING = 8
TYPE_OTHER = 9

# Training Timing IDs
TIMING_9 = 9 # od 00:06:01 do 00:06:30
TIMING_10 = 10 # od 00:06:31 do 00:07:00
TIMING_11 = 11  # od 00:06:01 i powyżej
TIMING_12 = 12  # od 00:07:01 i powyżej

# Running Training Type IDs
RUNNING_TYPE_NOT_SPECIFIED = 6

# context_names
CONTEXT_AUTH_EXCEPTION = 'auth_exception'
CONTEXT_HTTP_EXCEPTION = 'http_exception'
CONTEXT_RESULT_INPUT_TABLE = 'result_input_table'
CONTEXT_RESULT_OUTPUT_TABLE = 'result_output_table'
CONTEXT_TABLE = 'table'
CONTEXT_TRAINING = 'training'
CONTEXT_RUNNING_TRAINING = 'running_training'
CONTEXT_FORM_RESPONSE = 'form_response'
CONTEXT_FORM_USER = 'form_user'
CONTEXT_ADD_TRAINING_FORM = 'add_training_form'
CONTEXT_ADD_RUNNING_TRAINING_FORM = 'add_running_training_form'
CONTEXT_GENERATE_TRAINING_FORM = 'generate_training_form'
CONTEXT_SHOW_TRAINING_FORM = 'show_training_form'
CONTEXT_SHOW_FORM_RESPONSE = 'show_form_response'
CONTEXT_EXCEPTION = 'exception'

# model file names
DTM_MODEL_1KM = 'dtm_model_1km'
LR_MODEL_1KM = 'lr_model_1km'
KNR_MODEL_1KM = 'knr_model_1km'
DTM_MODEL_5KM = 'dtm_model_5km'
LR_MODEL_5KM = 'lr_model_5km'
KNR_MODEL_5KM = 'knr_model_5km'
DTM_MODEL_10KM = 'dtm_model_10km'
LR_MODEL_10KM = 'lr_model_10km'
KNR_MODEL_10KM = 'knr_model_10km'
DTM_MODEL_21KM = 'dtm_model_21km'
LR_MODEL_21KM = 'lr_model_21km'
KNR_MODEL_21KM = 'knr_model_21km'
DTM_MODEL_42KM = 'dtm_model_42km'
LR_MODEL_42KM = 'lr_model_42km'
KNR_MODEL_42KM = 'knr_model_42km'

# time columns constants
COLUMN_TIME_1KM_ID = 'time_1km_id'
COLUMN_TIME_5KM_ID = 'time_5km_id'
COLUMN_TIME_10KM_ID = 'time_10km_id'
COLUMN_TIME_21KM_ID = 'time_21km_id'
COLUMN_TIME_42KM_ID = 'time_42km_id'
