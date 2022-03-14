"""
Provides model for Teams (Groups)
"""
from django.db import models

__author__ = "Joseph Cato"

# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=100,  null=False, blank=False, unique=True)
    date_created = models.DateTimeField(verbose_name="date created" , auto_now_add=True) 
    point_total = models.IntegerField(default=0)

    def __str__(self):
        return self.name