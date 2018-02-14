from calendar import timegm
from datetime import datetime

from django.contrib.auth import authenticate
from django.core.exceptions import PermissionDenied

from django_auth_jwt_tenant import settings
from django_auth_jwt_tenant.compat import User


jwt_payload_handler = settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = settings.JWT_ENCODE_HANDLER
jwt_decode_handler = settings.JWT_DECODE_HANDLER
jwt_get_user_id_from_payload = settings.JWT_PAYLOAD_GET_USER_ID_HANDLER


def get_token(**credentials):
    """
    Generate JWT token to the pass in user with the credentials passed in.
    """
    token = None
    user = authenticate(**credentials)
    if user:
        if not user.is_active:
            msg = 'User account is disabled.'
            raise PermissionDenied(msg)

        payload = jwt_payload_handler(user)

        # Include original issued at time for a brand new token,
        # to allow token refresh
        if settings.JWT_ALLOW_REFRESH:
            payload['orig_iat'] = timegm(
                datetime.utcnow().utctimetuple()
            )

        token = jwt_encode_handler(payload)

    return token


def get_token_from_user(user: User):
    """
    Generate JWT token to the pass in user
    """
    assert user is not None, 'User must be provided'
    token = None
    if user:
        if not user.is_active:
            msg = 'User account is disabled.'
            raise PermissionDenied(msg)

        payload = jwt_payload_handler(user)

        # Include original issued at time for a brand new token,
        # to allow token refresh
        if settings.JWT_ALLOW_REFRESH:
            payload['orig_iat'] = timegm(
                datetime.utcnow().utctimetuple()
            )

        token = jwt_encode_handler(payload)

    return token
