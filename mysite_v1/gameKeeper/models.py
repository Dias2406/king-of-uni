from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify

# Create your models here.

class Building(models.Model):
    name 					= models.CharField(max_length=50, null=False, blank=False, unique=True)
    latitude 				= models.DecimalField(max_digits=10, decimal_places=5, null=False, blank=False)
    longitude 				= models.DecimalField(max_digits=10, decimal_places=5, null=False, blank=False)
    is_active               = models.BooleanField(default=False)
    is_captured             = models.BooleanField(default=False)

    slug 					= models.SlugField(blank=True, unique=True)

    def __str__(self):
	    return self.name

def pre_save_building_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = slugify(instance.name)

pre_save.connect(pre_save_building_receiver, sender=Building)