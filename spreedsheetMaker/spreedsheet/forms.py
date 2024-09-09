from django import forms
from django.forms import ModelForm
from .models import User 

class UserCreationForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

    def clean_username(self):
        username = self.cleaned_data.get('username')
        # check if username is already taken
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Username is already taken, please enter something else.')
        return username

    def clean_password(self):
        password = self.cleaned_data.get('password')
        # check if password is at least 8 characters long
        if len(password) < 8:
            raise forms.ValidationError('Password must be at least 8 characters long.')
        return password