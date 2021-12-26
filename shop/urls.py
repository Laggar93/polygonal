from django.urls import path
from . import views

urlpatterns = [
    # path('<slug:category_slug>/<slug:subcategory_slug>/<slug:item_slug>/', views.item_view, name='item_view'),
    # path('order/', views.order_view, name='order_view'),
    path('shop/<str:category_slug>/<str:subcategory_slug>/', views.subcategory_view, name='subcategory_view'),
    path('shop/<str:category_slug>/', views.category_view, name='category_view'),

]

# handler404 = views.error404
