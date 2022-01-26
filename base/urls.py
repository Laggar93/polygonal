from django.urls import path
from shop.views import handler404
from . import views

urlpatterns = [
    path('rules/', views.rules_view, name='rules'),
    path('offer/', views.offer_view, name='offer'),
    path('policy/', views.policy_view, name='policy'),

]

handler404 = handler404