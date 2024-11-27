# orders/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('customers/', views.customer_list, name='customer_list'),  # List customers
    path('orders/', views.order_list, name='order_list'),  # List orders
    path('add_customer/', views.add_customer, name='add_customer'),  # Add customer form
    path('add_order/', views.add_order, name='add_order'),  # Add order form
]
