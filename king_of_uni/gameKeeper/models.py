"""
Provides model for Building
"""
from datetime import datetime, tzinfo
from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify

__author__ = "Rob Campbell"

class Building(models.Model):
    name 					= models.CharField(max_length=50, null=False, blank=False, unique=True)
    latitude 				= models.DecimalField(max_digits=20, decimal_places=15, null=False, blank=False)
    longitude 				= models.DecimalField(max_digits=20, decimal_places=15, null=False, blank=False)
    streak                  = models.DecimalField(max_digits=1,decimal_places=0, default=1)
    is_active               = models.BooleanField(default=False)
    is_captured             = models.BooleanField(default=False)
    holder                  = models.CharField(max_length=50, default='Nobody')
    capture_date            = models.DateTimeField(blank=True, null=True)
    slug 					= models.SlugField(blank=True, unique=True)

    def buildingInfo(self):
        return self.name + " - held by: " + self.holder 
    def __str__(self):
	    return self.name




def pre_save_building_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = slugify(instance.name)

pre_save.connect(pre_save_building_receiver, sender=Building)