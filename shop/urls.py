from django.urls import path
from . import views
# from .views import handler404

urlpatterns = [
    path('shop/<str:category_slug>/<str:subcategory_slug>/', views.subcategory_view, name='subcategory_view'),
    path('shop/<str:category_slug>/', views.category_view, name='category_view'),
    path('shop/', views.first_category_for_url, name='first_category_for_url'),

]


# handler404 = handler404
