from django.urls import path
from shop.views import handler404
from . import views

urlpatterns = [
    path('contacts/', views.contact_view, name='contacts'),

]

handler404 = handler404
