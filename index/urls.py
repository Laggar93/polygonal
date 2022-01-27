from django.urls import path
from shop.views import handler404
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),

]

handler404 = handler404