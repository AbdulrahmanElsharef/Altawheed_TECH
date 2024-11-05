from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    list_display = ['__str__','note']
    list_filter = ['name']

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ['__str__','note']
    list_filter = ['name']

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['__str__','note']
    list_filter = ['name']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['__str__','note']
    list_filter = ['name']
    
@admin.register(Cus_Service)
class Cus_ServiceAdmin(admin.ModelAdmin):
    list_display = ['__str__','phone']
    list_filter = ['name',"phone"]
    
    
@admin.register(inquiry_Status)
class inquiry_StatusAdmin(admin.ModelAdmin):
    list_display = ['__str__','note']
    list_filter = ['inquiry']



@admin.register(FeedBack_Status)
class  FeedBack_StatusAdmin(admin.ModelAdmin):
    list_display = ['__str__','note']
    list_filter = ['feedback']
#_________________________________


@admin.register(City)
class  FeedBack_StatusAdmin(admin.ModelAdmin):
    list_display = ['__str__','city']
    list_filter = ['city']
#_________________________________


@admin.register(FeedBack)
class FeedBackAdmin(admin.ModelAdmin):
    list_display = ['Inquiry','Status',"client","phone",'Details','created_']
    list_filter = ['id','Inquiry',"Inquiry__client","Inquiry__client__phone",'Status','Details','Created']
    # list_filter = ['Order',"Sales",'Order','inquiry']
    # search_fields = ['client__phone']
    # exclude = ("InquiryId",)
    def created_(self,obj):
        return obj.Created.strftime("%d %m %Y %H %M %S")
    
    def client(self,obj):
        return obj.Inquiry.client
    
    def phone(self,obj):
        return obj.Inquiry.client.phone
    
    


class FeedBackInline(admin.TabularInline):
    model = FeedBack
    extra = 0
    list_display=('__str__','Inquiry','Status','Details','created_')
    def created_(self,obj):
        return obj.Created.strftime("%d %m %Y %H %M %S")
    
@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    inlines = [FeedBackInline]
    list_display = ['__str__','client',"phone",'request','source','status',"brand","category","inquiry","Details","created_"]
    list_filter = ['InquiryId','client','client__phone','source','status',"request","brand","category","inquiry","Details","Created"]
    # list_filter = ['Order',"Sales",'Order','inquiry']
    search_fields = ['client__phone']
    exclude = ("InquiryId",)
    def created_(self,obj):
        return obj.Created.strftime("%d %m %Y %H %M %S")
    
    def phone(self,obj):
        return obj.client.phone