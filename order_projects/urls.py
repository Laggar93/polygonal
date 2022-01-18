from django.urls import path

from shop.views import handler404
from . import views

urlpatterns = [
    path('projects/', views.projects_view, name='projects'),

]

handler404 = handler404
