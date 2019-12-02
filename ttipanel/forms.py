from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from.models import Paulapplication
from django import forms


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Paulapplication
        fields= "__all__"
