from django.db import models
from django.contrib.auth import get_user_model
from core.models import TimeStampMixin, PrimaryKeyAsUUIDMixin


class Post(TimeStampMixin, PrimaryKeyAsUUIDMixin):
    body = models.CharField(max_length=1000)
    user = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE)
