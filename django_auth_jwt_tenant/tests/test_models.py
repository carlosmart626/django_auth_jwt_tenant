# -*- coding: utf-8 -*-
import pytest

from django.contrib.auth.models import User

from django_auth_jwt_tenant.auth import get_token, get_token_from_user


@pytest.fixture
def internal_user():
    user = User(username='carlosmart', is_staff=True, is_superuser=True)
    user.set_password("123carlosmart123")
    user.save()


@pytest.mark.django_db
def test_get_user_token(internal_user):
    params = {
        'username': 'carlosmart',
        'password': '123carlosmart123'
    }
    token = get_token(**params)
    assert token is not None        


@pytest.mark.django_db
def test_get_user_token_from_user_object(internal_user):
    user = User.objects.get(username='carlosmart')
    token = get_token_from_user(user)
    assert token is not None        
