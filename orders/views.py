# orders/views.py
from django.shortcuts import render, redirect
from .models import Customer, Order
from .forms import CustomerForm, OrderForm  # Import forms to handle form data

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'orders/customer_list.html', {'customers': customers})

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'orders/order_list.html', {'orders': orders})

# Add customer view to handle customer creation form
def add_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')  # Redirect to customer list after successful submission
    else:
        form = CustomerForm()  # Create an empty form for the GET request
    return render(request, 'orders/add_customer.html', {'form': form})

# Add order view to handle order creation form
def add_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_list')  # Redirect to order list after successful submission
    else:
        form = OrderForm()  # Create an empty form for the GET request
    return render(request, 'orders/add_order.html', {'form': form})
