# -*- coding: utf-8 -*-

import pytest
from django.urls import reverse
from doubles import allow

from rest_framework import status
from rest_framework.exceptions import NotAuthenticated

from apps.accounts.api.v1.serializers.session import SessionSerializer
from apps.accounts.response_codes import INVALID_FACEBOOK_ACCESS_TOKEN
from apps.accounts.services.session import SessionService


@pytest.mark.django_db
class FacebookLoginTests:
    facebook_login_url = reverse('api-accounts:v1:facebook-login')

    def test_missing_token(self, api_client):
        response = api_client.post(self.facebook_login_url, {})
        response_json = response.json()
        assert 'access_token' in response_json
        assert response_json['access_token'][0]['code'] == 'required'

    def test_valid_token(self, api_client, test_user):
        allow(SessionService).process_facebook_token.and_return(test_user)

        login_data = {'access_token': 'valid_token'}
        response = api_client.post(self.facebook_login_url, login_data)
        response_json = response.json()

        assert response.status_code == status.HTTP_200_OK
        user_data = SessionSerializer(test_user).data
        assert response_json.keys() == user_data.keys()

    def test_invalid_token(self, api_client):
        allow(SessionService).process_facebook_token.and_raise(
            NotAuthenticated(**INVALID_FACEBOOK_ACCESS_TOKEN)
        )
        login_data = {'access_token': 'invalid_token'}
        response = api_client.post(self.facebook_login_url, login_data)
        response_json = response.json()

        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        assert response_json.get('code') == INVALID_FACEBOOK_ACCESS_TOKEN.get('code')

