from . import views
from django.urls import path

urlpatterns = [
    path('', views.contests, name='registrations.index'),
    path('show/<uuid>/', views.show_contest, name='registrations.show'),
    path('my', views.registrations, name='registrations.mine'),
]
