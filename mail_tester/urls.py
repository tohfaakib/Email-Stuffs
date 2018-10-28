from django.urls import path, include

from . import views

urlpatterns = [
    path('mail/', views.mail_tester, name='mail'),
    path('alive-mail/', views.alive_mail, name='alive_mail'),
]
