from django.db import models
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from Technical.models import Request,End_User,Vendor
#___________________________________________________________________
class City(models.Model):
    city = models.CharField(('City'),max_length=300,unique=True)
    note=models.CharField(("Note"), max_length=50,null=True,blank=True)
    def __str__(self) :
        return f"""{self.city}""" 
    class Meta:
        verbose_name_plural ="City"
        
        
class Source(models.Model):
    name = models.CharField(('Source'),max_length=300,unique=True)
    note=models.CharField(("Note"), max_length=50,null=True,blank=True)
    def __str__(self) :
        return f"""{self.name}""" 
    class Meta:
        verbose_name_plural ="Source"
        
        
class Status(models.Model):
    name = models.CharField(('Status'),max_length=300,unique=True)
    note=models.CharField(("Note"), max_length=50,null=True,blank=True)
    def __str__(self) :
        return f"""{self.name}""" 
    class Meta:
        verbose_name_plural ="Status"
        
        
class Brand(models.Model):
    name = models.CharField(('Brand'),max_length=50,unique=True)
    note=models.CharField(("Note"), max_length=50,null=True,blank=True)
    def __str__(self) :
        return f"""{self.name}"""
    
    class Meta:
        verbose_name_plural ="Brand"
        
        
class Category(models.Model):
    name = models.CharField(('Category'),max_length=50,unique=True)
    note=models.CharField(("Note"), max_length=50,null=True,blank=True)
    def __str__(self) :
        return f"""{self.name}"""
    
    class Meta:
        verbose_name_plural ="Category"



class inquiry_Status(models.Model):
    inquiry = models.CharField(('Inquiry'),max_length=50,unique=True)
    note=models.CharField(("Note"), max_length=50,null=True,blank=True)
    def __str__(self) :
        return f"""{self.inquiry}"""
    
    class Meta:
        verbose_name_plural ="inquiry_Status"
#_________________________________


class FeedBack_Status(models.Model):
    feedback = models.CharField(('feedback'),max_length=50,unique=True)
    note=models.CharField(("Note"), max_length=50,null=True,blank=True)
    def __str__(self) :
        return f"""{self.feedback}"""
    
    class Meta:
        verbose_name_plural ="FeedBack_Status"
        
class Cus_Service(models.Model):
    name = models.CharField(('name'),max_length=50,unique=True)
    phone=models.CharField(("Note"), max_length=50,null=True,blank=True)
    def __str__(self) :
        return f"""{self.name}"""
    
    class Meta:
        verbose_name_plural ="Cus_Service"
#_________________________________

class Inquiry(models.Model):
    Cus_Service=models.ForeignKey(get_user_model(), on_delete=models.PROTECT, related_name='Dr_Print_Order_Sales',null=True, blank=True) 
    InquiryId = models.IntegerField(null=True, blank=True)
    client=models.ForeignKey(End_User,related_name='Inquiry_client',on_delete=models.PROTECT)
    city=models.ForeignKey(City,related_name='Inquiry_City',on_delete=models.PROTECT,null=True, blank=True)
    branch=models.CharField(("Branch"), max_length=200,null=True,blank=True)
    source=models.ForeignKey(Source,related_name='Inquiry_Source',on_delete=models.PROTECT)
    status=models.ForeignKey(Status,related_name='Status_client',on_delete=models.PROTECT)
    request = models.ForeignKey(Request,related_name='request_Inquiry',on_delete=models.PROTECT,null=True, blank=True)
    account = models.ForeignKey(Vendor,related_name='Vendor_Inquiry',on_delete=models.PROTECT,null=True, blank=True)
    serial=models.CharField(("Serial"), max_length=50,null=True,blank=True)
    brand=models.ForeignKey(Brand,related_name='Inquiry_brand',on_delete=models.PROTECT)
    category=models.ForeignKey(Category,related_name='Inquiry_category',on_delete=models.PROTECT)
    inquiry =models.ForeignKey(inquiry_Status,related_name='inquiry_Status',on_delete=models.PROTECT)
    Details= models.TextField(("Details"),max_length=250,)
    Created = models.DateTimeField(auto_now_add=True)
    Note=models.CharField(("Note"), max_length=50,default='No_Note')
    
    def __str__(self) :
        return f"""INQ-{self.InquiryId}"""

    class Meta:
        verbose_name_plural ="Inquiry"
        
        
    def save(self, *args, **kwargs):
        if self.id is None:
            super().save(*args, **kwargs)
        if self.InquiryId is None:
            self.InquiryId = self.id
            super().save(*args, **kwargs)
      
#_______________________________________________________________________________
def user_directory(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    # return "{0}--{1}".format(instance.customer, filename)
    return f"{instance.Inquiry.client}--{filename}"
class FeedBack(models.Model):
    Inquiry = models.ForeignKey(Inquiry,related_name='FeedBack_Inquiry',on_delete=models.PROTECT)
    Status =models.ForeignKey(FeedBack_Status,related_name='Feedback_Status',on_delete=models.PROTECT)
    file=models.FileField(("File"), upload_to=user_directory, max_length=200)
    Details= models.TextField(("FeedBack"),max_length=250)
    Created = models.DateTimeField(auto_now_add=True)
    note=models.CharField(("Note"), max_length=50,default='No_Note')
    
    def __str__(self):
        return str(self.Inquiry)

    class Meta:
        verbose_name_plural ="FeedBack"

    def request(self):
        order_id= self.Inquiry.request
        return order_id
    
    # def sales_(self):
    #     order_sales= self.Inquiry.Sales
    #     return order_sales
#_______________________________________________________________________________

#