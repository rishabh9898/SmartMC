from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
# Register your models here.
from .models import *
from .forms import CreateForm
from import_export.admin import ImportExportModelAdmin

from embed_video.admin import AdminVideoMixin
from .models import Item


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
class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(Item, MyModelAdmin)
