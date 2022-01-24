from django.urls import path
from shop.views import handler404
from . import views

urlpatterns = [
    path('about/', views.about_view, name='about'),

]

handler404 = handler404