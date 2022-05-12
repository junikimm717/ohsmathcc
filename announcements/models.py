from django.db import models
import uuid

# Create your models here.

class Announcement(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    class Meta:
        ordering = ['-timestamp']
