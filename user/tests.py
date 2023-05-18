import pytest
from rest_framework.test import APIClient
from .models import User
from rest_framework import status
from rest_framework.response import Response
from conftest import testuser_email


@pytest.mark.django_db
def test_create_user() -> None:
    client = APIClient()
    request_data = {"email": "foo@example.com", "password": "pass"}
    response: Response = client.post(
        path="/api/user/create/", data=request_data, format="json"
    )
    assert response.status_code == status.HTTP_201_CREATED
    assert User.objects.filter(email=request_data["email"]).exists()


@pytest.mark.django_db
def test_get_user_no_auth(no_auth_client: APIClient) -> None:
    response: Response = no_auth_client.get(path="/api/user/")
    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db
def test_get_user_session_auth(session_auth_client: APIClient) -> None:
    response: Response = session_auth_client.get(path="/api/user/")
    assert response.status_code == status.HTTP_200_OK
    assert response.data["email"] == testuser_email


@pytest.mark.django_db
def test_get_user_jwt_auth(jwt_auth_client: APIClient) -> None:
    response: Response = jwt_auth_client.get(path="/api/user/")
    assert response.status_code == status.HTTP_200_OK
    assert response.data["email"] == testuser_email


@pytest.mark.django_db
def test_update_user(session_auth_client: APIClient, no_auth_client: APIClient) -> None:
    data = {"email": "nya@example.com", "password": "nekoneko"}
    update_response: Response = session_auth_client.put(
        path="/api/user/update/", data=data, format="json"
    )
    assert update_response.status_code == status.HTTP_200_OK

    token_response: Response = no_auth_client.post(
        path="/api/token/", data=data, format="json"
    )
    assert token_response.status_code == status.HTTP_200_OK
    assert token_response.data.get("access") is not None


@pytest.mark.django_db
def test_delete_user(session_auth_client: APIClient) -> None:
    response: Response = session_auth_client.delete("/api/user/delete/")

    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert not User.objects.filter(email=testuser_email).exists()
