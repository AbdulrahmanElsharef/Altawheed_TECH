from django.contrib import admin
from .models import Company_Details,Missions,Mission_Kind,Oil_Change,Oil_Detail,Car,Expenses_Detail

    
    
@admin.register(Missions)
class MissionsAdmin(admin.ModelAdmin):
    list_display =['mission','Officer','car','company',"order","author",'date']
    list_filter =['mission__name','Officer__name','car','company',"order","author",'date']
    search_fields =['detail','company',"order"]

    
#              Company_Details
@admin.register(Company_Details)
class Company_DetailsAdmin(admin.ModelAdmin): 
    list_display =['company','kind',"address",'location','phone','response',"work_hours"]
    list_filter=['company','kind',"response"]
    search_fields =['address','phone',]

    
    

 
# # #               Oil_Detail
@admin.register(Oil_Detail)
class Oil_DetailAdmin(admin.ModelAdmin): 
    list_display =['car',"Officer",'oil_kind','fuel_amount','litters','Car_meter','lastMeter','metres','date']
    list_filter=['car__car_number',"Officer__name",]
    exclude = ('lastMeter','metres')
    
    def litters(self,instance):
        litters = int(instance.fuel_amount/instance.car.car_tank.price)
        return litters
    
    def oil_kind(self,obj):
        kind = obj.car.car_tank.kind
        return kind
    
class Oil_ChangeAdmin(admin.ModelAdmin): 
    list_display =['car','oil_kind',"oil_name","rest_kilo",'Car_meter',"date"]
    list_filter=['car','oil_kind']
    search_fields=['car',]
    # def oil_rest(self,obj):
    #     rest = obj.rest_kilo
    #     return rest
    
admin.site.register(Oil_Change,Oil_ChangeAdmin)
    
# # #                 Car    
@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display =['car_kind','car_number',"Officer",'car_tank','record_date','end_date',"note",]
    list_filter=['car_kind','car_number','Officer',"car_tank",]


  
@admin.register(Expenses_Detail) 
class expenses_detailAdmin(admin.ModelAdmin):
    list_display =['car',"Officer",'expenses_kind',"cost",'detail','file']
    list_filter=['car',"Officer__name",'expenses_kind__name']

# #admin.site.register(expenses_detail,expenses_detailAdmin)




