from django.urls import path

from . import views

urlpatterns = [
    path('', views.events, name='times.events'),
    path('<eventid>/', views.eventform, name='times.eventform'),
    path('<eventid>/view', views.viewtimes, name='times.view'),
]

