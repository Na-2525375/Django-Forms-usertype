from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Person  
from django import forms


class SignupForm(UserCreationForm):
    
    USER_TYPE_CHOICES = (
    ('admin', 'Admin'),
    ('student', 'Student'),
    ('teacher', 'Teacher'),
)
    user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES, label='User Type')
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'user_type']
        labels = {
            'username': 'Username',
            'email': 'Email',
            'password1': 'Password',
            'password2': 'Confirm Password',
            'user_type': 'User Type',
        }

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        for field_name in ['username', 'email', 'password1', 'password2', 'user_type']:
            self.fields[field_name].widget.attrs.update({'class': 'form-control'})
            
class LoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')
    

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'age', 'address', 'family_member_count']

    def __init__(self, *args, **kwargs):
        super(PersonForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs.update({'class': 'form-control'})           