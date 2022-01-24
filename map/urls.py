from django.urls import path
from shop.views import handler404
from . import views

urlpatterns = [
    path('map/', views.map_view, name='map'),

]

handler404 = handler404