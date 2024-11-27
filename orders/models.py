from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')
    order_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, choices=[
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('shipped', 'Shipped'),
        ('canceled', 'Canceled')
    ])
    
    def __str__(self):
        return f'Order {self.id} by {self.customer}'
