from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _

# Create your models here.

ORDER_STATUS=(('Pending','Pending'),('Done','Done'),('Delivered','Delivered'))
ORDER_BRANCH=(('Cairo','Cairo'),('Alex','Alex'),('Asyut','Asyut'))
MESSAGE_KIND=(('Pending_MSG','Pending_MSG'),('Done_MSG','Done_MSG'),('Delivered_MSG','Delivered_MSG'),('FollowUP_MSG','FollowUP_MSG'))
WARRANTY=(('In_Warranty','In_Warranty'),('Out_Warranty','Out_Warranty'))
CONNECT=(('Phone','Phone'),('WatsApp','WatsApp'),('Messenger','Messenger'))
# DELIVERY_kind=(('In_Office','In_Office'),('Out_Office','Out_Office'),('At_Home','At_Home'))
RATE=(('راضى','راضى'),('غير_راضى','غير_راضى'),('يحتاج_تطوير','يحتاج_تطوير'))
CLIENT_kind=(('End_User','End_User'),('I_R_Client','I_R_Client'),('O_R_Client','O_R_Client'),('Out_Source','Out_Source'))


    
class End_User(models.Model):
    name=models.CharField(_("End_User"), max_length=50)
    phone=models.CharField(_("Phone"), max_length=25)
    email=models.EmailField(_("Email"), max_length=50,null=True,blank=True)
    
    note=models.CharField(_("User_Note"), max_length=50,default='No Note')
    
    def __str__(self):
        return str(self.name)


class Vendor(models.Model):
    name=models.CharField(_("company"), max_length=100,unique=True)
    logo=models.ImageField(_("Logo"), upload_to='Vendor',null=True,blank=True)
    note=models.CharField(_("Note"), max_length=50,default='No Note')
    def __str__(self):
        return str(self.name)


    
    
class Product(models.Model):
    barcode=models.CharField(_("Barcode"), max_length=50,unique=True)
    des=models.CharField(_("Description"), max_length=200)
    color=models.CharField(_("Color"), max_length=50)
    brand=models.CharField(_("Brand"), max_length=50)
    sku=models.CharField(_("Sku"), max_length=50)
    note=models.CharField(_("Note"), max_length=50,default='No Note')

    def __str__(self):
        return str(self.barcode)
    
    
    
class Issue(models.Model)  :
    name=models.CharField(_("issue"), max_length=25,unique=True)
    note=models.CharField(_("Note"), max_length=50,default='No Note')
    def __str__(self):
        return str(self.name)

class Technician(models.Model)  :
    name=models.CharField(_("technician"), max_length=25,unique=True)
    note=models.CharField(_("Note"), max_length=50,default='No Note')
    def __str__(self):
        return str(self.name)
    


class Action(models.Model)  :
    name=models.CharField(_("action"), max_length=25,unique=True)
    note=models.CharField(_("Note"), max_length=50,default='No Note')
    def __str__(self):
        return str(self.name)

    
class Request(models.Model):
    branch=models.CharField(_("Req_Branch"), max_length=50,choices=ORDER_BRANCH,default=ORDER_BRANCH[0])
    status=models.CharField(_("Req_Status"), max_length=50,choices=ORDER_STATUS,default=ORDER_STATUS[0])
    client=models.CharField(_("client_kind"), max_length=50,choices=CLIENT_kind,default=ORDER_STATUS[0])
    End_User = models.ForeignKey(End_User, on_delete=models.SET_NULL,null=True,blank=True,verbose_name=_('Client_Name'),related_name='Request_client')
    Vendor = models.ForeignKey(Vendor, on_delete=models.PROTECT,verbose_name=_('Vendor'),related_name='Request_Vendor')
    received_date=models.DateField(_("Received_Date"),default=timezone.now)
    created=models.DateTimeField(("Created"), auto_now=True,)
    updated=models.DateTimeField(("updated"), auto_now_add=True,)
    note=models.CharField(_("Note"), max_length=50,default='No_Note')
    def __str__(self):
        return f"REQ0{str(self.id)}"
    
    def purchase(self):
        date=self.request_Failer_Detail.purchase_date
        return date
    def Delivery_d(self):
        date=self.request_Delivery.delivery_date
        return date
        
class Failer_Detail(models.Model)  :
    request=models.ForeignKey(Request, on_delete=models.PROTECT,verbose_name=_('Request'),related_name='request_Failer_Detail')
    product=models.ForeignKey(Product, on_delete=models.PROTECT,verbose_name=_('Product'),related_name='Failer_Detail_Product')
    serial_in=models.CharField(_("S.N_IN"), max_length=25)
    active=models.CharField(_("Active"), max_length=25,choices=WARRANTY,default=WARRANTY[0])
    purchase_date=models.DateField(_("Purchase_Date"),null=True,blank=True)
    invoice=models.ImageField(_("invoice"), upload_to='Invoice',null=True,blank=True)
    issue=models.ForeignKey(Issue, on_delete=models.PROTECT,verbose_name='Issue',related_name='Issue_name')
    detail=models.CharField(_("Detail"),max_length=300,default='Write Issue Detail')
    ref=models.CharField(_("REF_NUM"), max_length=25,default='No_Ref')
    created=models.DateTimeField(("Created"), auto_now=True,)
    updated=models.DateTimeField(("updated"), auto_now_add=True,)
    note=models.CharField(_("Note"), max_length=50,default='No_Note')
    
    def __str__(self):
        return str(self.request)
    
    def company(self):
        name=self.request.Vendor
        return name
    
    def User(self):
        name=self.request.End_User
        return name
    
    # def Delivery(self):
    #     date=self.request.request_Delivery.delivery_date
    #     return date
    
    

class Action_Detail(models.Model)  :
    request=models.ForeignKey(Request, on_delete=models.PROTECT,verbose_name=_('Request'),related_name='request_Action_Detail')
    product=models.ForeignKey(Product, on_delete=models.PROTECT,verbose_name=_('Product'),related_name='Action_Detail_Product')
    serial_out=models.CharField(_("S.N_Out"), max_length=50)
    action=models.ForeignKey(Action, on_delete=models.PROTECT,verbose_name='Action',related_name='Action_name')
    detail=models.CharField(_("Detail"),max_length=300,default='Write Action Detail')
    delivery_date=models.DateField(_("Delivery_Date"),null=True,blank=True)
    technician=models.ForeignKey(Technician, on_delete=models.PROTECT,verbose_name='Technician',related_name='Action_Technician')
    cost=models.IntegerField(_("Cost"),default=0)
    last_serial=models.CharField(_("last_S.N"), max_length=50,default='No Serail')
    ref=models.CharField(_("REF_NUM"), max_length=25,default='No_Ref')
    created=models.DateTimeField(("Created"), auto_now=True,)
    updated=models.DateTimeField(("updated"), auto_now_add=True,)
    note=models.CharField(_("Note"), max_length=50,default='No Note')
    def __str__(self):
        return str(self.request)
    
    def company(self):
        name=self.request.Vendor
        return name
    
    def User(self):
        name=self.request.End_User
        return name
    
    # def Delivery(self):
    #     date=self.request__request_Delivery.delivery_date
    #     return date
class Follow_Up(models.Model):
    request=models.ForeignKey(Request, on_delete=models.SET_NULL,null=True,blank=True,verbose_name=_('Request'),related_name='request_Follow_Up')
    connect=models.CharField(_("Connect"), max_length=50,choices=CONNECT,default=ORDER_STATUS[0])
    msg_kind=models.CharField(_("Message"), max_length=50,choices=MESSAGE_KIND,default=RATE[0])
    comment=models.TextField(_("Comment"),max_length=500,null=True,blank=True)
    rate=models.CharField(_("Rate"), max_length=50,choices=RATE,default=RATE[0])
    note=models.CharField(_("Note"), max_length=50,default='No Note')
    def __str__(self):
        return str(self.request)

    class Meta:
        verbose_name_plural = "Follow_Up"
    

class Report(models.Model):
    request=models.ForeignKey(Request, on_delete=models.SET_NULL,null=True,blank=True,verbose_name=_('Request'),related_name='request_Report')
    product=models.ForeignKey(Product, on_delete=models.SET_NULL,null=True,blank=True,verbose_name=_('Product'),related_name='Report_Product')
    serial_out=models.CharField(_("S.N_Out"), max_length=50,null=True,blank=True)
    complain=models.TextField(_("Complain"),max_length=500)
    Report=models.TextField(_("Report"),max_length=500)
    advice=models.TextField(_("Advice"), max_length=500)
    note=models.CharField(_("Note"), max_length=50)
    def __str__(self):
        return str(self.request)




class SpareName(models.Model) :
    Part_Name=models.CharField(("Part"), max_length=25,unique=True)
    def __str__(self):
        return str(self.Part_Name) 
    class Meta:
        verbose_name_plural = "SparePart"


class SpareItem(models.Model):
    serial=models.CharField(_("Serial"), max_length=30,unique=True)
    product=models.ForeignKey(Product, on_delete=models.PROTECT,verbose_name=_('Product'),related_name='SpareItem_Product')
    Spare_1=models.ForeignKey(SpareName, on_delete=models.SET_NULL,null=True,blank=True,verbose_name=_('Spare'),related_name='SpareName1')
    Status_1 = models.BooleanField(("Status"),default=False)
    Spare_2=models.ForeignKey(SpareName, on_delete=models.SET_NULL,null=True,blank=True,verbose_name=_('Spare'),related_name='SpareName2')
    Status_2 = models.BooleanField(("Status"),default=False)
    Spare_3=models.ForeignKey(SpareName, on_delete=models.SET_NULL,null=True,blank=True,verbose_name=_('Spare'),related_name='SpareName3')
    Status_3 = models.BooleanField(("Status"),default=False)
    Spare_4=models.ForeignKey(SpareName, on_delete=models.SET_NULL,null=True,blank=True,verbose_name=_('Spare'),related_name='SpareName4')
    Status_4 = models.BooleanField(("Status"),default=False)
    Spare_5=models.ForeignKey(SpareName, on_delete=models.SET_NULL,null=True,blank=True,verbose_name=_('Spare'),related_name='SpareName5')
    Status_5 = models.BooleanField(("Status"),default=False)
    Spare_6=models.ForeignKey(SpareName, on_delete=models.SET_NULL,null=True,blank=True,verbose_name=_('Spare'),related_name='SpareName6')
    Status_6 = models.BooleanField(("Status"),default=False)
    Spare_7=models.ForeignKey(SpareName, on_delete=models.SET_NULL,null=True,blank=True,verbose_name=_('Spare'),related_name='SpareName7')
    Status_7 = models.BooleanField(("Status"),default=False)
    Spare_8=models.ForeignKey(SpareName, on_delete=models.SET_NULL,null=True,blank=True,verbose_name=_('Spare'),related_name='SpareName8')
    Status_8 = models.BooleanField(("Status"),default=False)
    note=models.CharField(_("Note"), max_length=50,default='No Note')
    def __str__(self):
        return str(self.serial)
    class Meta:
        verbose_name_plural = "SpareItem"


class SpareAction(models.Model):
    serial=models.ForeignKey(SpareItem, on_delete=models.SET_NULL,null=True,blank=True,verbose_name=_('serial'),related_name='SpareItem')
    request=models.ForeignKey(Request, on_delete=models.PROTECT,verbose_name=_('Request'),related_name='SpareAction_Detail')
    action=models.CharField(_("Action"), max_length=100)
    note=models.CharField(_("Note"), max_length=50,default='No Note')

    def __str__(self):
        return str(self.serial)
    class Meta:
        verbose_name_plural = "SpareAction"
