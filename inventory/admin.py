from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
from .models import *

# Register your models here.

@admin.register(Laptop,Mobile,USB,MemmoryCard, Charger,Handfree,Datacabels,Speakers)
class viewAdmin(ImportExportActionModelAdmin):
    exclude = ('id',)