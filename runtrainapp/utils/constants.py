# List Athlete Activities (getLoggedInAthleteActivities)
# getLoggedInAthleteActivities URL
LIST_ACTIVITIES_URL = 'https://www.strava.com/api/v3/athlete/activities'

# refresh token URL Strava
REFRESH_TOKEN_STRAVA_URL = 'https://www.strava.com/oauth/token'

# Amount of activities returned in one call
PER_PAGE = 200

# Account Provider Name
STRAVA_ACCOUNT_PROVIDER = 'strava'

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

# Running Training Type IDs
RUNNING_TYPE_NOT_SPECIFIED = 6

# context_names
CONTEXT_AUTH_EXCEPTION = 'auth_exception'
CONTEXT_HTTP_EXCEPTION = 'http_exception'
CONTEXT_TABLE = 'table'
CONTEXT_TRAINING = 'training'
