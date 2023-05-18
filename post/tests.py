from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from rest_framework.response import Response
import pytest
from .models import Post
from conftest import testuser_email

# Create your tests here.


@pytest.fixture
@pytest.mark.django_db
def post_a(user):
    return Post.objects.create(user=user, body="igyo")


@pytest.fixture
@pytest.mark.django_db
def post_b(user):
    return Post.objects.create(user=user, body="nyanpuppu")


@pytest.mark.django_db
class TestPostApi:
    def test_get_posts_no_auth(self, no_auth_client: APIClient) -> None:
        response: Response = no_auth_client.get(path="/api/post/")
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_create_post(self, session_auth_client: APIClient) -> None:
        data = {"body": "igyo"}
        response: Response = session_auth_client.post(
            path="/api/post/", data=data, format="json"
        )
        print(response.data)
        assert response.status_code == status.HTTP_201_CREATED
        assert Post.objects.filter(body="igyo").exists()

    def test_get_posts(self, session_auth_client: APIClient, post_a, post_b) -> None:
        response: Response = session_auth_client.get(path="/api/post/")
        assert response.status_code == status.HTTP_200_OK
        assert "count" in response.data
        assert "next" in response.data
        assert "previous" in response.data
        assert "results" in response.data
        assert response.data["count"] == 2

    def test_get_posts_filter(
        self, session_auth_client: APIClient, post_a, post_b
    ) -> None:
        response: Response = session_auth_client.get(
            path="/api/post/", data={"body": "nyan"}
        )
        assert response.status_code == status.HTTP_200_OK
        assert "count" in response.data
        assert "next" in response.data
        assert "previous" in response.data
        assert "results" in response.data
        assert response.data["count"] == 1

    def test_get_post(self, session_auth_client: APIClient, post_a: Post) -> None:
        id = post_a.id
        response: Response = session_auth_client.get(path=f"/api/post/{id}/")
        assert response.status_code == status.HTTP_200_OK
        assert response.data["body"] == "igyo"
        assert response.data["user"]["email"] == testuser_email
