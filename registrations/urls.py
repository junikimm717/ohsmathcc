from . import views
from django.urls import path

urlpatterns = [
    path('', views.contests, name='registrations.index'),
    path('show/<uuid>/', views.show_contest, name='registrations.show'),
    path('signedup/<uuid>/', views.registrations_for_contest, name='registrations.signedup'),
    path('my', views.registrations, name='registrations.mine'),
]
