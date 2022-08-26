from django import forms
from .customer import Customer

class SignUpForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [ 'first_name', 'last_name', 'email', 'password' ]
