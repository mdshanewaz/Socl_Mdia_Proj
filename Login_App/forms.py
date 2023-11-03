from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class CreateUserView(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        user = User
        fields = ('email', 'username', 'password1', 'password2')