import pytest
from user.models import User
from dataclasses import dataclass
from rest_framework.test import APIClient
from rest_framework.response import Response

testuser_email = "alice@example.com"
testuser_password = "nyanpuppu"


@pytest.fixture
@pytest.mark.django_db
def user():
    return User.objects.create_user(email=testuser_email, password=testuser_password)


@pytest.fixture
def no_auth_client():
    return APIClient()


@pytest.fixture
def session_auth_client(user):
    client = APIClient()
    client.login(email=testuser_email, password=testuser_password)
    return client


@pytest.fixture
def jwt_auth_client(user):
    client = APIClient()
    data = {"email": testuser_email, "password": testuser_password}
    response: Response = client.post(path="/api/token/", data=data, format="json")
    token = response.data["access"]
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
    return client
