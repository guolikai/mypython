from __future__ import unicode_literals

from django.db import models
from django.db.models.fields import CharField
from _tkinter import create
from MySQLdb import DATETIME

# Create your models here.
class UserInfo(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    
class Hostname(models.Model):
    hostname = models.CharField(max_length=256)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)