from django.db import models
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from Technical.models import Request,End_User,Vendor
#___________________________________________________________________


class Sales(models.Model):
    name = models.CharField(('Name'),max_length=20,unique=True)
    phone = models.IntegerField(('Phone'),unique=True,default='No_Phone')
    
    def __str__(self) :
        return f"""{self.name}""" 
    class Meta:
        verbose_name_plural ="Sales"

#_________________________________

class Order_Status(models.Model):
    status = models.CharField(('Status'),max_length=20,unique=True)
    note=models.CharField(("Note"), max_length=150,default='No_Note')
    def __str__(self) :
        return f"""{self.status}""" 
    class Meta:
        verbose_name_plural ="Status"

#_________________________________


class EMPLOYEE(models.Model):
    name = models.CharField(('Name'),max_length=300,unique=True)
    note=models.CharField(("Note"), max_length=150,default='No_Note')

    def __str__(self) :
        return f"""{self.name}""" 
    class Meta:
        verbose_name_plural ="EMPLOYEE"

#_________________________________


class Order(models.Model):
    order= models.CharField(("Sales Order"), max_length=20)
    account=models.ForeignKey(Vendor, on_delete=models.PROTECT,verbose_name=('Account'),related_name='Order_Account')
    sales=models.ForeignKey(Sales,verbose_name=('Sales'),related_name='Order_sales',on_delete=models.PROTECT)
    Created = models.DateTimeField(auto_now=True)
    note=models.CharField(("Note"), max_length=150,default='No_Note')
    
    def __str__(self) :
        return f"""{self.order}"""

    class Meta:
        verbose_name_plural ="Order"
        
        

#_______________________________________________________________________________

class Coordinator (models.Model):
    order=models.ForeignKey(Order,related_name='Coordinator_Order',on_delete=models.PROTECT)
    quantity=models.IntegerField(("Quantity"),default=0)
    Status =models.ForeignKey(Order_Status,related_name='Coordinator_Status',on_delete=models.PROTECT)
    date=models.DateTimeField(("Date Out"), default=timezone.now)
    # time=models.TimeField(("Time"), default=timezone.now)
    Created = models.DateTimeField(auto_now=True)
    note=models.CharField(("Note"), max_length=150,default='No_Note')
    
    def __str__(self):
        return str(self.order)

    class Meta:
        verbose_name_plural ="Coordinator"


    # def sales_(self):
    #     order_sales= self.Inquiry.Sales
    #     return order_sales
#_______________________________________________________________________________

WORK_HOURS = (
    ('2', '2'),
    ('4', '4'),
    ('6', '6'),
    ('8', '8'),
    ('10', '10'),
)
class Warehouse (models.Model):
    order=models.ForeignKey(Order,related_name='Warehouse_Order',on_delete=models.PROTECT,null=True,blank=True)
    # time=models.TimeField(("Time"), default="00:00:00",null=True,blank=True)
    work=models.CharField(max_length=10, choices=WORK_HOURS,null=True,blank=True)
    Preparing =models.ForeignKey(Order_Status,related_name='Preparing_Status',on_delete=models.PROTECT,null=True,blank=True)
    Author=models.ForeignKey(EMPLOYEE,related_name='Preparing_Author',on_delete=models.PROTECT,null=True,blank=True)
    Status =models.ForeignKey(Order_Status,related_name='Order_Status',on_delete=models.PROTECT,null=True,blank=True)
    Receiver=models.ForeignKey(EMPLOYEE,related_name='Receiver_Author',on_delete=models.PROTECT,null=True,blank=True)
    quantity=models.IntegerField(("Quantity"),default=0)
    Created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    note=models.CharField(("Note"), max_length=150,default='No_Note')

    
    def __str__(self):
        return str(self.order)

    class Meta:
        verbose_name_plural ="Warehouse"


class Delivery(models.Model):
    order=models.ForeignKey(Order,related_name='Delivery_Order',on_delete=models.PROTECT)
    Author=models.ForeignKey(EMPLOYEE,related_name='Delivery_Author',on_delete=models.PROTECT)
    Receiver_QT=models.IntegerField(("Receiver_QT"),default=0)
    time=models.TimeField(("Time"), null=True,blank=True)
    Created = models.DateTimeField(auto_now=True)
    note=models.CharField(("Note"), max_length=150,default='No_Note')
    def __str__(self):
        return str(self.order)

    class Meta:
        verbose_name_plural ="Delivery"



class Receiving(models.Model):
    order=models.ForeignKey(Order,related_name='Receiving_Order',on_delete=models.PROTECT)
    Author=models.ForeignKey(EMPLOYEE,related_name='Receiving_Author',on_delete=models.PROTECT)
    client_QT=models.IntegerField(("Client_QT"),default=0)
    refund_QT=models.IntegerField(("Refund_QT"),default=0)
    date=models.DateField(("Refund Date"), null=True,blank=True)
    collection=models.IntegerField(("collection"),default=0)
    Created = models.DateTimeField(auto_now =True)
    note=models.CharField(("Note"), max_length=150,default='No_Note')
    def __str__(self):
        return str(self.order)

    class Meta:
        verbose_name_plural ="Receiving"


