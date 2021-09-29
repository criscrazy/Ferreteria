from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import *

# Register your models here.

###
class resourceProducto(resources.ModelResource):
    class Meta:
        model =producto  #nombre tabla

class AdminProducto(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['codigo']
    list_display = ['name','description','price']
    resource_class = resourceProducto

admin.site.register(producto, AdminProducto)
###

###
class resourceStock(resources.ModelResource):
    class Meta:
        model =stock  #nombre tabla

class AdminStock(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['amount']
    resource_class = resourceStock

admin.site.register(stock, AdminStock)
###

###
class resourcesell(resources.ModelResource):
    class Meta:
        model =sell  #nombre tabla

class AdminSell(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['name_client']
    list_display = ['date_buy', 'amount']
    resource_class = resourcesell

admin.site.register(sell, AdminSell)
###