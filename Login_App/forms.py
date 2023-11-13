from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from Login_App.models import UserprofileModel

class CreateUserForm(UserCreationForm):
    email = forms.EmailField(required=True, label="", widget=forms.TextInput(attrs={'placeholder':'Email'}))
    username = forms.CharField(required=True, label="", widget=forms.TextInput(attrs={'placeholder':'Username'}))
    password1 = forms.CharField(required=True, label="", widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
    password2 = forms.CharField(required=True, label="", widget=forms.PasswordInput(attrs={'placeholder':'Password Confirmation'}))

    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2')


class EditProfile(forms.ModelForm):
    date_of_birth = forms.DateField(widget=forms.TextInput(attrs={'type':'date',}))

    class Meta:
        model = UserprofileModel
        exclude = ('user', )
