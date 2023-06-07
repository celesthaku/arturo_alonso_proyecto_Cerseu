from django.urls import path
from . import views

urlpatterns = [
    path('meseros/', views.meseros, name='meseros'),


]