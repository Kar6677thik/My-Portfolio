from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'port-home'),
    path('about/', views.about, name = 'port-about'),
    path('projects/', views.projects, name = 'port-projects'),
    path('contact/', views.contact, name = 'port-contact'),
]