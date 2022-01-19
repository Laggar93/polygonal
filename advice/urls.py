from django.urls import path

from shop.views import handler404
from . import views

urlpatterns = [
    path('advice/', views.advice_view, name='advice'),
    path('advice-item/', views.advice_item_view, name='advice-item'),

]

handler404 = handler404
