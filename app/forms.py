from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Record

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput


# - register/create a user
class CreateUserForm(UserCreationForm):    
    class Meta:        
        model = User
        fields = ['username', 'password1', 'password2']
        
# - login a user

class LoginForm(AuthenticationForm):
    
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())
    
    def __init__(self, *args, **kwargs):
        authentication_form = kwargs.pop('authentication_form', AuthenticationForm)
        super().__init__(*args, **kwargs)
        
        
# - Add an Appointment
        
        
class CreateRecordForm(forms.ModelForm):

    class Meta:

        model = Record
        fields = ['fname', 'email', 'email', 'phone', 'date', 'time', 'note',]
        
        
# - Update an Appointment
        
        
class UpdateRecordForm(forms.ModelForm):

    class Meta:

        model = Record
        fields = ['fname', 'email', 'email', 'phone', 'date', 'time', 'note',]
        
