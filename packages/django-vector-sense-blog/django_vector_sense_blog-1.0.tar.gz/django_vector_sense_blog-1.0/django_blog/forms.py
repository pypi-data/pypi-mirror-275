# forms.py
from django import forms
from .models import UserAddress
import os

# Form for user address input
class UserAddressForm(forms.ModelForm):
    class Meta:
        model = UserAddress
        fields = [ 'house_number', 'street', 'city', 'zipcode', 'country']
        
    # Add this method to make fields not required
    def __init__(self, *args, **kwargs):
        super(UserAddressForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.required = False
            