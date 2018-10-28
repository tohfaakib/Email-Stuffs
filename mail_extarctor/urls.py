from django.urls import path

from . import views

urlpatterns = [
    path('', views.extractor, name='extractor'),
    path('collector', views.collector, name='collector')

]