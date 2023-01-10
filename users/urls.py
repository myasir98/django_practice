from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'users'
urlpatterns = [
    path('login/', views.login_action, name='login'),
    # path('signup'),
]
