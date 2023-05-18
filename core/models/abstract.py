from django.db import models
import uuid


class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class PrimaryKeyAsUUIDMixin(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)

    class Meta:
        abstract = True
