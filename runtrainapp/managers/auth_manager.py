import requests

from allauth.socialaccount.models import SocialToken
from datetime import timedelta
from django.utils import timezone
from runtrainapp.utils.constants import *
from runtrainapp.managers.exception_manager import *


# Get active token for user and specific provider
def get_active_token_from_user(user, account_provider):
    token_obj = SocialToken.objects.filter(account__user=user, account__provider=account_provider)

    if not token_obj.exists():
        raise raise_auth_exception(user)

    token_obj = token_obj[0]
    if is_token_expired(token_obj):
        token = refresh_token(token_obj, account_provider)
    else:
        token = token_obj.token

    return token


# Check if token is expired
def is_token_expired(token_obj):
    return timezone.now() > token_obj.expires_at


# General refresh token
def refresh_token(token_obj, account_provider):
    new_token = None
    new_token_expire_date = None

    # Refresh token for specific provider
    if account_provider == STRAVA_ACCOUNT_PROVIDER:
        new_token, new_token_expire_date = refresh_strava_token(token_obj)

    save_new_token(token_obj, new_token, new_token_expire_date)

    return new_token


# Refresh token for Strava account
def refresh_strava_token(token_obj):
    secret_token = token_obj.token_secret

    app = token_obj.app
    client_id = app.client_id
    client_secret = app.secret

    params = {
        "client_id": client_id,
        "client_secret": client_secret,
        "grant_type": "refresh_token",
        "refresh_token": secret_token
    }

    response = requests.request(
        'POST',
        REFRESH_TOKEN_STRAVA_URL,
        params=params
    )

    if response.status_code != 200:
        raise Exception(response.status_code)

    response_json = response.json()
    new_token = response_json['access_token']
    expires_in = response_json['expires_in']

    # Seconds from response added to current datetime to get token expire date
    new_token_expire_date = timezone.now() + timedelta(seconds=expires_in)

    return new_token, new_token_expire_date


# Save new token - return is_saved, new_token
def save_new_token(token_obj, new_token, new_token_expire_date):
    is_saved = False

    if token_obj is None or new_token is None or new_token_expire_date is None:
        return is_saved, new_token

    token_obj.token = new_token
    token_obj.expires_at = new_token_expire_date
    token_obj.save()

