from django.db import models
from django.db.models import F
from django.contrib.auth.models import User
import uuid
from . import utils

# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField(null=True, blank=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    class Meta:
        ordering = [F('date').asc(nulls_first=True)]

class AvailableTime(models.Model):
    time = models.CharField(max_length=2, choices=utils.TIME_OPTIONS)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)