from django.urls import path
from . import views

urlpatterns = [
    path('platos/', views.platos, name='platos'),


]