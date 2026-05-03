from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('servicii/', views.services, name='services'),
    path('despre/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]