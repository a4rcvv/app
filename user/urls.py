from django.urls import path
from .views import CreateUserView, RetrieveUserView, UpdateUserView, DestroyUserView

urlpatterns = [
    path("create/", CreateUserView.as_view()),
    path("", RetrieveUserView.as_view()),
    path("update/", UpdateUserView.as_view()),
    path("delete/", DestroyUserView.as_view()),
]
