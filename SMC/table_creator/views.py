from django.shortcuts import render
from .models import Item
# Create your views here.
def home(request):
    obj = Item.objects.all()
    return render(request, 'table_creator/landing.html', {'obj':obj})