from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget, AdminSplitDateTime

from embed_video.fields import EmbedVideoField

category_choice = (
		('1', '1'),
		('2','2'),
		('3','3'),
		('4','4'),
	)

category_choice_2 = (
		('2', '2'),
	)
category_choice_3 = (
		('3', '3'),
	)

category_choice_4 = (
		('4', '4'),
	)

# class ApplicantData(models.Model):
    # scheduled_at = models.DateTimeField(null=True, blank=True)


# class SmartMC(models.Model):
	# place_in = models.ForeignKey(Category, on_delete=models.CASCADE)
	
class SmartMC(models.Model):
	name = models.CharField("Please Enter your Full Name",max_length=50, blank=True, null=True)
	pill_Box1 = models.CharField("Add the Box you want to store pill in ",max_length=50, blank=True, null=True,choices=category_choice)
	total_quantity=models.IntegerField(" Total Amount of Pills ",default='0', blank=True, null=True)
	quantity = models.IntegerField("Pills you wish to take now",default='0', blank=True, null=True)
	
	# pill_Box2 = models.CharField(max_length=50, blank=True, null=True,choices=category_choice)
	# pill_Box3 = models.CharField(max_length=50, blank=True, null=True,choices=category_choice)
	# pill_Box4 = models.CharField(max_length=50, blank=True, null=True,choices=category_choice)
	date_now=models.DateTimeField(auto_now=True)
	day_name = models.CharField("Please Enter the name of the day",max_length=50, blank=True, null=True)
	email=models.EmailField(max_length=200)
	
	# export_to_CSV = models.BooleanField(default=False)

	def __str__(self):
		return self.name

class Item(models.Model):
    video = EmbedVideoField()

 
