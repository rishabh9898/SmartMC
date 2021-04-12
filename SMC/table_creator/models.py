from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget, AdminSplitDateTime

from embed_video.fields import EmbedVideoField

category_choice = (
		('Pill Box-1', 'Pill Box-1'),
		('Pill Box-2', 'Pill Box-2'),
		
	)

class Category(models.Model):
	name_of_box = models.CharField(max_length=50, blank=True, null=True)
	def __str__(self):
		return self.name_of_box
class SmartMC(models.Model):
	place_in = models.ForeignKey(Category, on_delete=models.CASCADE)
	
class SmartMC(models.Model):
	name = models.CharField(max_length=50, blank=True, null=True)
	quantity = models.IntegerField(default='0', blank=True, null=True)
	place_in = models.ForeignKey(Category, on_delete=models.CASCADE,blank=True)
	receive_by = models.CharField(max_length=50, blank=True, null=True)
	phone_number = models.CharField(max_length=50, blank=True, null=True)
	date=models.DateField(default=timezone.now)
	date_now=models.DateTimeField(auto_now=True)
	email=models.EmailField(max_length=200)
	last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	# export_to_CSV = models.BooleanField(default=False)

	def __str__(self):
		return self.name

class Item(models.Model):
    video = EmbedVideoField()

 
