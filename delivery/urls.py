from django.urls import path
from shop.views import handler404
from . import views

urlpatterns = [
    path('delivery/', views.delivery_main_view, name='delivery'),

]

handler404 = handler404
