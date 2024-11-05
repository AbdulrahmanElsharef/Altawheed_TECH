from django.contrib import admin

from .models import  *
from datetime import datetime, timedelta

@admin.register(Sales)
class SalesAdmin(admin.ModelAdmin):
    list_display = ['name','phone']
    list_filter = ['name','phone']
    
@admin.register(Order_Status)
class Order_StatusAdmin(admin.ModelAdmin):
    list_display = ['status','note']
    list_filter = ['status']
    
    
@admin.register(EMPLOYEE)
class EMPLOYEEAdmin(admin.ModelAdmin):
    list_display = ['name','note']
    list_filter = ['name']
    
    
@admin.register(Coordinator)
class CoordinatorAdmin(admin.ModelAdmin):
    list_display = ['order','quantity',"Status","date","Created","note"]
    list_filter = ['order__order','quantity',"Status","date","Created","note"]
    
    
@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ['order',"work","Preparing","Author","Status","Receiver","quantity","Created","updated","note"]
    list_filter = ['order__order',"work","Preparing","Author","Status","Receiver","quantity","Created","updated",]
    # def time_out(self, obj):
    #     if obj.time:
    #         new=obj.time.time() + 2 * 60 * 60
    #         # new= datetime.datetime.strptime(f"{time}:00:00", "%H:%M:%S").time()
    #         # obj.time+=new
    #         # if obj.work==2:   
    #         #     new=time_obj = datetime.datetime.strptime("2:00:00", "%H:%M:%S").time()
    #         #     obj.time+=new
    #         # elif obj.work==4:   
    #         #     new=time_obj = datetime.datetime.strptime("4:00:00", "%H:%M:%S").time()
    #         #     obj.time+=new
    #         # elif obj.work==6:   
    #         #     new=time_obj = datetime.datetime.strptime("6:00:00", "%H:%M:%S").time()
    #         #     obj.time+=new
    #         # else :   
    #         #     new=time_obj = datetime.datetime.strptime("8:00:00", "%H:%M:%S").time()
    #         #     obj.time+=new
    #         # new_time = time+timedelta(hours=2)
    #         return obj.time
    #     # else:
    #     #     return None


@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = ['order','Author',"Receiver_QT","time","Created","note"]
    list_filter = ['order__order','Author',"Receiver_QT","time","Created","note"]
@admin.register(Receiving)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = ['order','Author',"client_QT","refund_QT","date","collection","Created","note"]
    list_filter = ['order','Author',"client_QT","refund_QT","date","collection","Created","note"]









# Register your models here.
class WarehouseTabularInline(admin.TabularInline):
     model = Warehouse
     extra = 0
class DeliveryTabularInline(admin.TabularInline):
     model = Delivery
     extra = 0
class CoordinatorTabularInline(admin.TabularInline):
     model = Coordinator
     extra = 0
class ReceivingTabularInline(admin.TabularInline):
     model = Receiving
     extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [CoordinatorTabularInline,WarehouseTabularInline,DeliveryTabularInline,ReceivingTabularInline]  
    list_display =['order','account',"sales",'Created','note']
    list_filter=['order','account',"sales",'Created']
    search_fields=('note',)