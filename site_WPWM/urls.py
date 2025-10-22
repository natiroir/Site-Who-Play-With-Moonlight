from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('actualite', views.actualite, name='actualite'),
    path('reproducteur', views.reproducteur, name='reproducteur'),
    path('chiots', views.chiots, name='chiots'),
    path('communaute', views.communaute, name='communaute'),
    path('contact', views.contact, name='contact'),
]
