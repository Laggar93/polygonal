from django.urls import path
from . import views
from .views import handler404

urlpatterns = [
    path('shop/<str:category_slug>/<str:subcategory_slug>/', views.subcategory_view, name='subcategory_view'),
    path('shop/<str:category_slug>/', views.category_view, name='category_view'),
    path('shop/', views.first_category_for_url, name='first_category_for_url'),
    path('shop/<str:category_slug>/<str:subcategory_slug>/<str:item_slug>', views.catalog_item, name='catalog_item'),
    path('cart/', views.order_view, name='cart'),
    path('update_card/', views.update_basket_view, name='update_basket_view')
]


handler404 = handler404
