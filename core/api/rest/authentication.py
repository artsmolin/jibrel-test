from django.utils.translation import gettext_lazy as _
from django.conf import settings
from rest_framework import exceptions
from rest_framework.authentication import BasicAuthentication


class TestBasicAuthentication(BasicAuthentication):
    def authenticate_credentials(self, user_id, password, request=None):
        if user_id == settings.BASE_AUTH_USER and password == settings.BASE_AUTH_PASSWORD:
            return None, None
        raise exceptions.AuthenticationFailed(_('Invalid username/password.'))
