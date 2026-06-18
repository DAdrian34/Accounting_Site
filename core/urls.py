from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('servicii/', views.services, name='services'),
    path('despre/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

    path(
        'politica-de-confidentialitate/',
        views.privacy_policy,
        name='privacy_policy'
    ),
    path(
        'politica-cookies/',
        views.cookie_policy,
        name='cookie_policy'
    ),
    path(
        'termeni-si-conditii/',
        views.terms_conditions,
        name='terms_conditions'
    ),
]