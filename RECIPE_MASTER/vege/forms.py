from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

class UserCreationform(UserCreationForm):
    def __init__(self,*args,**kwargs):
        super(UserCreationform,self).__init__(*args,*args, **kwargs)
        
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control'
        }))
    
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control'
        }))

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control'
        }))
    
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'class':'form-control'
        }))

    password1 = forms.CharField(widget = forms.PasswordInput(attrs={
        'class':'form-control'
    }))
    password2 = forms.CharField(widget = forms.PasswordInput(attrs={
        'class':'form-control'
    }))

    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password1','password2']


class Authenticationform(AuthenticationForm):
    def __init__(self,*args,**kwargs):
        super(Authenticationform,self).__init__(*args,*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control'
        }))
    password = forms.CharField(widget = forms.PasswordInput(attrs={
        'class':'form-control'
    }))