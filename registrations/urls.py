from . import views
from django.urls import path

urlpatterns = [
    path('', views.contests, name='registrations.index'),
]
