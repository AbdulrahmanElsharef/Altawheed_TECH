from django.db import models
import datetime
from datetime import date
from django.utils import timezone

LOCATIONS_KIND=(('مخزن','مخزن'),('الإدارة','الإدارة'),('محل','محل'))        
CAR_TANK=(('بنزين','بنزين'),('سولار','سولار'))
CAR_OIL=(('700','700'),('1000','1000'),('3000','3000'),('5000','5000'),('10000','10000'))
Maintains= (('مشتريات','مشتريات'),('صيانة','صيانة'),('اخرى','اخرى'))    


class Delevry_Officer(models.Model):
    name=models.CharField((" المندوب"), max_length=50)
    phone=models.CharField((" التليفون"), max_length=11)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "مندوب تسليم "
        

class Car_Tank(models.Model):
    kind=models.CharField(("نوع الوقود"), max_length=50,choices=CAR_TANK)
    price=models.DecimalField(("سعر الوقود"), max_digits=5, decimal_places=2)
    
    def __str__(self):
        return self.kind
    
    class Meta:
        verbose_name_plural = "انواع الوقود"


class Mission_Kind(models.Model):
    name=models.CharField(("العملية"), max_length=50)
    note=models.CharField(("ملاحظات"), max_length=50,null=True,blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "انواع العمليات"



        
        
class Expenses_Kind(models.Model):
    name=models.CharField((" المصروف"), max_length=50)
    note=models.CharField(("ملاحظات"), max_length=50,default="no-note")
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "انواع المصروفات"