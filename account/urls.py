from django.urls import path
from django.shortcuts import render
from . import views


app_name = 'account'

urlpatterns = [
    path('register/', views.register_user, name='register'),
    path('email-verification-sent/', lambda request: render(
        request, 'account/email/email-verification-sent.html'),
         name='email-verification-sent'),
]

