from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('join', views.join_meeting, name='join_meeting'),
]
