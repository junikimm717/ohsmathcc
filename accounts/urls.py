from django.urls import path,include
from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [
    #path('', include('django.contrib.auth.urls'), name='accouunts'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('profile/', views.profile, name='profile'),
]
