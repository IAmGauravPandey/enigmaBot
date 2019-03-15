from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Messages(models.Model):
    #user=models.OneToOneField(User,on_delete=models.CASCADE)
    messages=models.CharField(max_length=1000,default='')
    date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.messages