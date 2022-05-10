from django.contrib import admin

# Register your models here.
from .models import Registration, Contest

admin.site.register(Registration)
admin.site.register(Contest)
