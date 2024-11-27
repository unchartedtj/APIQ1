from django import forms
from .models import Customer, Order

# Form for creating or updating a Customer
class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'email', 'phone_number']
        # Add widgets or labels if needed
        # Example:
        # widgets = {
        #     'email': forms.EmailInput(attrs={'placeholder': 'Enter your email'}),
        # }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Example: Customizing the labels of form fields
        self.fields['first_name'].label = 'First Name'
        self.fields['last_name'].label = 'Last Name'

# Form for creating or updating an Order
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer', 'total_amount', 'status']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Example: Adding custom labels or validation
        self.fields['total_amount'].widget.attrs.update({'placeholder': 'Total Amount'})
