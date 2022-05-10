from django.db import models
import uuid
from django.contrib.auth.models import User

# Create your models here.

class Contest(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    deadline = models.DateField()
    description = models.TextField()

class Registration(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE)
    class Meta:
        ordering = ['-timestamp']
