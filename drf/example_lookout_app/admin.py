from django.contrib import admin

from django.contrib import admin
from .models import Lookout 

class LookoutAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'area', 'elevation', 'climate']

admin.site.register(Lookout, LookoutAdmin)

