from django.db import models
import datetime
from datetime import date
from django.utils import timezone

LOCATIONS_KIND=(('مخزن','مخزن'),('الإدارة','الإدارة'),('محل','محل'))  
CAR_OIL=(('700','700'),('1000','1000'),('3000','3000'),('5000','5000'),('10000','10000'))
      



from APP_DATA.models import Car_Tank,Delevry_Officer,Mission_Kind,Expenses_Kind
from Technical.models import Vendor
        
# ____________________Company_Details__________________________
class Company_Details(models.Model):
    company=models.ForeignKey(Vendor,verbose_name='اسم الشركة', on_delete=models.PROTECT,related_name="company_details")
    kind=models.CharField(("المكان"), max_length=50,choices=LOCATIONS_KIND)
    address=models.CharField(("عنوان الشركة"), max_length=500)
    location=models.CharField(("موقع الشركة"), max_length=500)
    phone=models.CharField(("تليفون المسؤول"),max_length=14,null=True,blank=True)
    response=models.CharField(("اسم المسؤول"),max_length=25,null=True,blank=True)
    work_hours=models.CharField(("مواعيد العمل"),max_length=25,null=True,blank=True)
    
    def __str__(self):
        return str(self.company)
    class Meta:
        verbose_name_plural = "مواقع الشركات"

# _____________________________________________________________________


# _________________________CAR__________________________


class Car(models.Model):
    car_kind=models.CharField(("نوع السيارة"), max_length=30)
    car_number=models.CharField(("رقم السيارة"), max_length=30)
    car_model=models.CharField(("موديل السيارة"), max_length=30)
    car_motor=models.CharField((" رقم الماتور"), max_length=50,default='Motor_No')
    car_chassis=models.CharField(("رقم الشاسية "), max_length=50,default='Chassis_No')
    car_tank=models.ForeignKey(Car_Tank, verbose_name=("نوع الوقود"),related_name='car_tank', on_delete=models.PROTECT)
    Officer=models.ForeignKey(Delevry_Officer,verbose_name=("مندوب التسليم"), max_length=50,related_name='car_officer',on_delete=models.PROTECT,null=True,blank=True)
    record_date=models.DateField(("بداية الترخيص"), auto_now=False, auto_now_add=False)
    end_date=models.DateField(("انتهاء الترخيص"), auto_now=False, auto_now_add=False)
    ADS_date=models.DateField(("بداية الاعلان"), auto_now=False, auto_now_add=False)
    ADS_END=models.DateField(("انتهاء الاعلان"), auto_now=False, auto_now_add=False)
    # today=models.DateField(default=date.today)
    note=models.CharField(("ملاحظات"), max_length=20,default='NO_NOTE')

    def get_current_day():
    # """
    # Returns the current day as a string in the format "YYYY-MM-DD".
    # Args:
    #     None
    # Returns:
    #     str: The current day in the format "YYYY-MM-DD".
    # """
        today = datetime.date.today()
        return today.strftime("%Y-%m-%d")
    def End_Date(self):
        end_date = self.end_date
        diff = self.end_date - self.get_current_day
        ENDS=int(diff.days)
        return ENDS
    
    def END_ADS(self):
        end_date = self.ADS_END
        diff = self.end_date - self.get_current_day
        days_ADS=int(diff.days)
        return days_ADS
    
    def __str__(self):
        return f"{str(self.car_kind)}--{str(self.car_number)}"
    
    class Meta:
        verbose_name_plural = "السيارات"

# ____________________________________________________________________

# _____________________ Missions_______________________

class Missions(models.Model):
    mission=models.ForeignKey(Mission_Kind,verbose_name=("نوع العملية"),related_name='Mission_Kind', max_length=50,on_delete=models.PROTECT)
    Officer=models.ForeignKey(Delevry_Officer,verbose_name=("المندوب"), max_length=50,related_name='Mission_officer',on_delete=models.PROTECT)
    car=models.ForeignKey(Car, verbose_name=("رقم السيارة"),related_name='Missions_car', on_delete=models.PROTECT,null=True,blank=True)
    company=models.ForeignKey(Vendor, verbose_name=(" الشركة"),related_name='Missions_company', on_delete=models.PROTECT,null=True,blank=True)
    order=models.CharField(("الاوردر"), max_length=100)
    author=models.CharField(("المسئول"), max_length=100)
    detail=models.TextField(("تفاصيل العملية"), max_length=300)
    date=models.DateField(("تاريخ "),  auto_now_add=True)
    def __str__(self):
        return str(self.Officer)
    class Meta:
        verbose_name_plural = "العمليات"
    
# ________________________________________________________________________

#_______________________Oil_Detail_______________________
class Oil_Detail(models.Model):
    car=models.ForeignKey(Car, verbose_name=("السيارة"),related_name='car_Oil_Detail', on_delete=models.PROTECT)
    Officer=models.ForeignKey(Delevry_Officer,verbose_name=("مندوب التسليم"),related_name='Oil_Detail_officer', max_length=50,on_delete=models.PROTECT,null=True,blank=True)
    fuel_amount=models.IntegerField(("مبلغ الوقود"))
    Car_meter=models.IntegerField(("قراءة العداد"),)
    date=models.DateField(("التاريخ"), auto_now=False, auto_now_add=False)
    lastMeter=models.IntegerField(("عداد سابق"),null=True,blank=True)
    metres=models.IntegerField(("عدد الكيلو"),null=True,blank=True)

       
    def save(self, *args, **kwargs):
        last = Oil_Detail.objects.filter(car=self.car).last()
        if last or self.metres:
            self.lastMeter=int(last.Car_meter)
            self.metres=self.Car_meter-self.lastMeter
        else:
            self.lastMete=0
            self.metres=0
        super(Oil_Detail, self).save(*args, **kwargs) # Call the real save() method           

    
    class Meta:
        verbose_name_plural = "استهلاك الوقود"
        
    def __str__(self):
        return str(self.car)


        
    
class Oil_Change(models.Model):
    car=models.ForeignKey(Car, verbose_name=("السيارة"),related_name='car_Oil_Change', on_delete=models.PROTECT)
    oil_kind=models.CharField(("نوع الزيت"), max_length=50,choices=CAR_OIL)
    oil_name=models.CharField((" الزيت"), max_length=100)
    Car_meter=models.IntegerField(("قراءة العداد"),default=0)
    date=models.DateField(("التاريخ"), auto_now=False, auto_now_add=False)
    note=models.CharField(("ملاحظات"), max_length=300,default='no note')
    
    def __str__(self):
        return str(self.car)

    class Meta:
        verbose_name_plural =  "تغيير الزيت"
    


    def rest_kilo(self):
        if self.pk:
            last = Oil_Detail.objects.filter(car=self.car).last()
            if self.oil_kind == '3000':
                kilos=3000+int(self.Car_meter)
                diff=int(kilos-last.Car_meter)
            elif self.oil_kind == '5000':
                kilos=5000+int(self.Car_meter)
                diff=int(kilos-last.Car_meter)
            elif self.oil_kind == '10000':
                kilos=10000+int(self.Car_meter)
                diff=int(kilos-last.Car_meter)
            return int(diff)
        




    
class Expenses_Detail(models.Model):
    car=models.ForeignKey(Car, verbose_name=("السيارة"),on_delete=models.PROTECT,related_name='car_Expenses',null=True,blank=True)
    Officer=models.ForeignKey(Delevry_Officer,verbose_name=("مندوب التسليم"), max_length=50,on_delete=models.PROTECT,null=True,blank=True)
    expenses_kind=models.ForeignKey(Expenses_Kind ,on_delete=models.PROTECT,verbose_name=("نوع المصروف"),related_name='expenses_name')
    detail=models.CharField(("تفاصيل المصروف"), max_length=300)
    cost=models.DecimalField(("التكلفة"),max_digits=8,decimal_places = 2)
    file=models.FileField(("تحميل ملف"), upload_to="expenses_files",null=True,blank=True)
    date=models.DateField(("تاريخ المصروفات"),auto_now_add=True)
    note=models.CharField(("ملاحظات"), max_length=50,default="no-note")

    def __str__(self):
        return str(self.car)
    
    class Meta:
        verbose_name_plural = "تفاصيل المصروفات"        


    
    
    
  

