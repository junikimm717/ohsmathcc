from django.db import models
from django.contrib.auth.models import User
import uuid
from . import utils

# Create your models here.

TIME_OPTIONS = zip(map(str, range(1, 14)), iter(utils.ScheduleTime(6, 0)))
class AvailableTime:
    time = models.CharField(max_length=2, choices=TIME_OPTIONS)
    person = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    