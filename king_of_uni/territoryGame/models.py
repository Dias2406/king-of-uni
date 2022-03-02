"""
Provides model for Territory capture
"""
from django.db import models
from gameKeeper.models import Building
from account.models import Account

__author__ = "Jakupov Dias"

# Create your models here.
class TerritoryCapture(models.Model):
    comment             = models.CharField(max_length=200, blank= True)
    territory_name      = models.ForeignKey(Building, verbose_name="Territories", default = 0, on_delete=models.SET_DEFAULT)
    username            = models.ForeignKey(Account, verbose_name="Users", default = 0, on_delete=models.SET_DEFAULT)

    def __str__(self):
        return self.comment
