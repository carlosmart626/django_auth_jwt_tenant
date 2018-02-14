import json
import pytest

from django.contrib.auth.models import User

from django_auth_jwt_tenant.auth import get_token_from_user


@pytest.fixture
def internal_user():
    user = User(username='carlosmart', is_staff=True, is_superuser=True)
    user.set_password("123carlosmart123")
    user.save()


def test_view_unauthorized(client):
    response = client.get('/api/', HTTP_ACCEPT='text/html')
    assert response.status_code == 401


@pytest.mark.django_db
def test_view_authorized(client, internal_user):
    user = User.objects.get(username='carlosmart')
    token = get_token_from_user(user)
    print("token", token)
    response = client.get('/api/', AUTHORIZATION='Bearer {}'.format(token))
    print(response)
    assert False
    assert response.status_code == 401



