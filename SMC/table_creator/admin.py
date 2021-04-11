from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
# Register your models here.
from .models import *
from .forms import CreateForm
from import_export.admin import ImportExportModelAdmin


class CreateAdmin(admin.ModelAdmin):
   list_display = ['name', 'email', 'quantity','date','place_in']
   form = CreateForm
   list_filter = ['name']
   search_fields = ['name', 'email']
# @admin.register(UserDetail)

# class usrdet(ImportExportModelAdmin):
# 	pass

# admin.site.register(SmartMC,CreateAdmin)
@admin.register(SmartMC)
class usrdet(ImportExportModelAdmin):
	pass


admin.site.register(Category)