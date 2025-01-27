from django import forms
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.forms.widgets import RadioSelect
from .models import Createaccount,Payment
from creditcards.forms import CardNumberField, CardExpiryField, SecurityCodeField


class Register(UserCreationForm):
    class Meta:
        model = Createaccount
        fields = ['name','email','password1','password2','date_of_birth','account']
        widgets = {'account': forms.RadioSelect(),'date_of_birth':forms.DateInput(attrs={'type':'date','max':datetime.now().date()})

        }

class Login(AuthenticationForm): 
    username =  forms.CharField(widget=forms.TextInput())
    password =  forms.CharField(widget=forms.PasswordInput())
        

class Bookings(forms.Form):
    date = forms.DateField(widget=forms.DateInput(attrs={'type':'date','min':datetime.now().date()}))
    adult = forms.IntegerField(min_value=0)
    children = forms.IntegerField(min_value=0)
    infants = forms.IntegerField(min_value=0)



class PaymentForm(forms.Form):
    model = Payment
    cc_number = CardNumberField(label='Card Number')
    cc_expiry = CardExpiryField(label='Expiration Date')
    cc_code = SecurityCodeField(label='CVV/CVC')