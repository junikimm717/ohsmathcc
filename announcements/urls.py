from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='announcements.index'),
    path('show/<uuid>', views.show_announcement, name='announcements.show'),
]
