from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget, AdminSplitDateTime
from django.contrib.auth.models import User
import csv
from table_creator.models import *
from table_creator.forms import CreateForm
from django.shortcuts import render, redirect
from .models import Item

# Create your views here.
# def setup(request):
# 	if request.method=='POST':
# 		fm=Reg(request.POST)
# 		if fm.is_valid():
# 			print('Form Validated')
# 	else:
# 		fm=Reg()
# 	return render(request, 'table_creator/setup.html',{'form':fm})

def home(request):
	obj = Item.objects.all()
	return render(request, 'table_creator/landing.html',{'obj':obj})

# def setup(request):
# 	form = 'List of entry'
# 	queryset = SmartMC.objects.all()
# 	context = {
# 		"form": form,
# 		"queryset": queryset,
# 	}
# 	return render(request, "table_creator/setup.html", context)

def add_items(request):
	form = CreateForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('/')
	context = {
		"form": form,
		"title": "Added Item to our database",
	}
	return render(request, "table_creator/add_items.html", context)

def about(request):
    return render(request, 'table_creator/about_us.html')

def learn(request):
    return render(request, 'table_creator/shop_learn.html')

