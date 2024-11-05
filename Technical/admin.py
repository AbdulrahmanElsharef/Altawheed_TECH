from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
# ImportExportModelAdmin



@admin.register(End_User)
class End_UserAdmin(admin.ModelAdmin):
    list_display =['id','name','phone','email','note',]
    list_filter=['name','phone','email']
    
    
@admin.register(Vendor)
class VendorAdmin(ImportExportModelAdmin):
    list_display =['id','name','logo','note']
    list_filter=['name',]


@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    list_display =['id','barcode','des','color','brand','sku','note']
    list_filter=['barcode','brand','color','sku']
    
    
@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    list_display =['id','name','note']
    
@admin.register(Technician)
class TechnicianAdmin(admin.ModelAdmin):
    list_display =['id','name','note']
     
@admin.register(Action)
class ActionAdmin(admin.ModelAdmin):
    list_display =['id','name','note']



#class Follow_UpTabularInline(admin.TabularInline):
     #model = Follow_Up
class ActionTabularInline(admin.TabularInline):
     model = Action_Detail
     extra = 0
class IssueTabularInline(admin.TabularInline):
     model = Failer_Detail
     extra = 0
#class ReportTabularInline(admin.TabularInline):
     #model = Report

  
@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    inlines = [IssueTabularInline,ActionTabularInline]  
    list_display =['__str__','status',"branch",'client','End_User','Vendor','received_date','note',"created","updated"]
    list_filter=['id','status',"branch",'client','End_User','End_User__phone','Vendor__name','received_date',]
    search_fields=('note',)
    


@admin.register(Failer_Detail)
class Failer_DetailAdmin(admin.ModelAdmin):
    list_display =['__str__','product','serial_in','active','invoice','purchase_date','issue','User','company',"created","updated"]
    list_filter=["request__id",'product__barcode','serial_in','active','purchase_date','issue__name','request__End_User','request__Vendor__name',"ref"]
    
    
    
@admin.register(Action_Detail)
class Action_DetailAdmin(admin.ModelAdmin):
    list_display =['__str__','product','serial_out',"last_serial",'action','technician','delivery_date','cost',"ref",'User','company',"created","updated"]
    list_filter=["request__id",'product__barcode','serial_out',"last_serial",'action__name','technician__name','delivery_date','request__End_User','request__Vendor__name',"ref"]



@admin.register(Follow_Up)
class Follow_UpAdmin(admin.ModelAdmin):
    list_display =['__str__','connect','msg_kind','comment','rate','note']
    list_filter=['request','connect','msg_kind','rate']

    
@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display =['__str__',"serial_out",'complain','Report','advice','note']
    list_filter=['request',"serial_out"]


@admin.register(SpareName)
class SpareNameAdmin(admin.ModelAdmin):
    list_display =['id','Part_Name']

class SpareActionTabularInline(admin.TabularInline):
    model=SpareAction
    extra = 0
@admin.register(SpareItem)
class SpareItemAdmin(ImportExportModelAdmin):
    inlines = [SpareActionTabularInline,]
    extra=0
    list_display =['serial','product',"Spare_1","Status_1","Spare_2","Status_2","Spare_3","Status_3","Spare_4","Status_4","Spare_5","Status_5","Spare_6","Status_6","Spare_7","Status_7","Spare_8","Status_8"]
    list_filter=['serial','product']
    #list_editable =("Status_1",'Status_2','Status_3','Status_4','Status_5','Status_6',"Status_7","Status_8")
    #list_filter=['serial','product',"Spare_1",'Spare_2','Spare_3','Spare_4','Spare_5','Spare_6',"Spare_7","Spare_8"]
    search_fields=["Spare_1__Part_Name","Spare_2__Part_Name","Spare_3__Part_Name","Spare_4__Part_Name","Spare_5__Part_Name","Spare_6__Part_Name","Spare_7__Part_Name","Spare_8__Part_Name"]


@admin.register(SpareAction)
class SpareActionAdmin(admin.ModelAdmin):
    list_display =['serial','request',"action","note"]
    list_filter =['serial','request',"action","note"]
    

    

