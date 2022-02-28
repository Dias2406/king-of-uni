from dataclasses import Field
from django.db import models

# Create your models here.


class Group(models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey('account.Account', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True) 
    point_total = models.IntegerField(default=0) 
    
