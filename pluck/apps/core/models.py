from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import JSONField
from django.contrib.auth.models import AbstractUser


class Request(models.Model):
    user_id = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    description = models.TextField()
    body = JSONField()
    headers = JSONField()

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(
        default=timezone.now, blank=True, null=True)

    def publish(self):
        self.created_at = self.updated_at = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Response(models.Model):
    user_id = models.ForeignKey('auth.User')
    request_id = models.ForeignKey(Request)
    body = JSONField()
    headers = JSONField()

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(
        default=timezone.now, blank=True, null=True)

    def publish(self):
        self.created_at = self.updated_at = timezone.now()
        self.save()

    def __str__(self):
        return self.title
