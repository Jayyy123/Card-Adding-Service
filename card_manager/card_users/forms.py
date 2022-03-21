from .models import UserAccount,User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm


class UserAccountForm(ModelForm):
    class Meta:
        model = UserAccount
        fields = ['first_name','last_name', 'username', 'email', 'profile_picture', 'date_of_birth', 'bank_information', 'gender']


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
