from django.db import models
from django import forms

class User(models.Model):
    nick_name = models.CharField(max_length=40)
    email = models.CharField(max_length=100)
    def __str__(self):
        return "%s" % (self.nick_name)
