from django.urls import path

from shop.views import handler404
from . import views

urlpatterns = [
    path('advice/', views.advice_view, name='advice'),
    path('advice/<str:advice_page_slug>', views.advice_item_view, name='advice_item_view'),

]

handler404 = handler404
