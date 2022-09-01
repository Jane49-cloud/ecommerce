from django import forms
from .customer import Customer
from django.contrib.auth.forms import AuthenticationForm
customer = Customer.objects.all()

class CustomAuthenticationForm(AuthenticationForm):
    def confirm_login_allowed(self, customer):
        if not customer.is_active or not customer.is_validated:
            raise forms.ValidationError('There was a problem with your login.', code='invalid_login')

class SignUpForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [ 'first_name', 'last_name', 'email', 'phone', 'password' ]


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=100)
    