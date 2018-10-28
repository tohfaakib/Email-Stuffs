from django.urls import path, include

from email_collector import views

urlpatterns = [
    path('email-collector/', views.email_collector, name='email_collector'),
    path('collected-list/', views.collected_list, name='collected_list'),
]
