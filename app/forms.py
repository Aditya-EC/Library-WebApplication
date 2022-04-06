from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name=forms.CharField(max_length=50,help_text='Required',widget=forms.TextInput(attrs={'placeholder':'FirstName'}))
    last_name=forms.CharField(max_length=50,help_text='Required',widget=forms.TextInput(attrs={'placeholder':'LastName','required':'none'}))
    email=forms.EmailField(max_length=200,help_text='Required',widget=forms.TextInput(attrs={'placeholder':'Email'}))
    class Meta:
        model=User
        widgets={
                 'username':forms.TextInput(attrs={'placeholder':'Username'}),
                 }
        fields=('first_name','last_name','email','password1','password2')
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'})
