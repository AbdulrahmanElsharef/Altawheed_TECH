from django.contrib import admin
from .models import Delevry_Officer,Car_Tank,Mission_Kind,Expenses_Kind
from import_export.admin import ImportExportModelAdmin
from Technical.models import Vendor

    

    
    
@admin.register(Delevry_Officer)
class Delevry_OfficerAdmin(admin.ModelAdmin):
    list_display = ["name","phone"]
    list_filter = ["name","phone"]
@admin.register(Car_Tank)
class Car_TankAdmin(admin.ModelAdmin):
    list_display = ["kind","price"]
@admin.register(Mission_Kind)
class Mission_KindAdmin(admin.ModelAdmin):
    list_display = ["name","note"]
@admin.register(Expenses_Kind)
class Expenses_KindAdmin(admin.ModelAdmin):
    list_display = ["name","note"]

