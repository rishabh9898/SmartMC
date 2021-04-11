from django.contrib import admin
from django.urls import include, path
from . import views
from django.views.i18n import JavaScriptCatalog

urlpatterns = [
    path('', views.home, name='home'),
    # path('setup/',views.setup,name='setup'),
    path('setup/',views.add_items,name='setup'),

    # path('Add-info/', views.add_items, name='Add-info'),
    # path('jsi18n',JavaScriptCatalog.as_view(),name='js-catalog'),
    # path('setup/', views.setup), 

]