from django.contrib import admin
from .models import Farmdata

# Register your models here.

class FarmAdmin(admin.ModelAdmin):
	list_display = ("year","province", "crop", "type_db", "account",)

admin.site.register(Farmdata, FarmAdmin)