from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import Messages,Query
from django.db import models

class MessageForm(forms.ModelForm):
    class Meta:
        model=Messages
        fields=(
            'messages',
        )
Queries=[
    ('man','Man'),
    ('ssh','Ssh'),
    ('mind-game','Mind-Game'),
    ('hangman','Hangman'),
    ('scrabble','Scrabble'),
    ('todo','Todo'),
    ('calculator','Calculator'),
    ('news','News'),
    ('dictionary','Dictionary'),
    ('news','News'),
    ('cricket','Cricket'),
    ('help','Help'),
]
class QueryForm(forms.Form):
    query=forms.CharField(label="Select your Query",widget=forms.Select(choices=Queries))