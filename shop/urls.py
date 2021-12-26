from django.urls import path
from . import views
# from .views import handler404_view

urlpatterns = [
    # path('<slug:category_slug>/<slug:subcategory_slug>/<slug:item_slug>/', views.item_view, name='item_view'),
    # path('order/', views.order_view, name='order_view'),
    # path('shop/', views.handler404_view, name='handler404_view'),
    path('shop/<str:category_slug>/<str:subcategory_slug>/', views.subcategory_view, name='subcategory_view'),
    path('shop/<str:category_slug>/', views.category_view, name='category_view'),
    path('shop/', views.first_category_for_url, name='first_category_for_url'),

]


# handler404 = handler404_view
