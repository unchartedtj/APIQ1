# orders/admin.py
from django.contrib import admin
from .models import Customer, Order

# Register Customer and Order models
admin.site.register(Customer)
admin.site.register(Order)
