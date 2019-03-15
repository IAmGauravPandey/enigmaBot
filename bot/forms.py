from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import Messages
from django.db import models

class MessageForm(forms.ModelForm):
    class Meta:
        model=Messages
        fields=(
            'messages',
        )