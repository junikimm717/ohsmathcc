from django.contrib import admin
from .models import AvailableTime, Event

# Register your models here.
admin.site.register(AvailableTime)
admin.site.register(Event)