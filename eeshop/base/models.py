from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

today = datetime.today()

year = today.year
month = today.month
day = today.day

datenow = str(month)+'/'+str(day)+'/'+str(year)

# Create your models here.

class Product(models.Model):
    user = models.ForeignKey(User,on_delete = models.SET_NULL,null = True)
    name = models.CharField(max_length=200,null = True, blank = True)
    image = models.ImageField(null=True, blank=True, default='/placeholder.png') 
    brand = models.CharField(max_length=200,null = True, blank = True)
    category = models.CharField(max_length=200,null = True, blank = True)
    description = models.TextField(null=True, blank=True)
    # rating = models.DecimalField(max_digits = 7,decimal_places=2, null= True, blank=True)
    # numReviews = models.IntegerField(null=True, blank=True, default=0)
    # price = models.DecimalField(max_digits = 7,decimal_places=2,null= True, blank=True)
    # countInStock = models.IntegerField(null=True, blank=True, default=0)
    createdAt = models.DateTimeField(auto_now_add=True)
    _id =  models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self._id)


class Platform_data(models.Model):
    
    product_id = models.ForeignKey(Product,on_delete = models.SET_NULL,null = True) 
    #product_id = models.IntegerField(null=True, blank=True, default=0)
    user = models.ForeignKey(User,on_delete = models.SET_NULL,null = True)
    _id =  models.AutoField(primary_key=True, editable=False)
    
    # platform_id = models.IntegerField(null=True, blank=True, default=1)
    platform_name = models.CharField(max_length=200,null = True, blank = True, default='Amazon')
    # platform_image=models.ImageField(null=True, blank=True) 

    price = models.DecimalField(max_digits = 7,decimal_places=2,null= True, blank=True, default=0.0)
    countInStock = models.IntegerField(null=True, blank=True, default=0)
    rating = models.DecimalField(max_digits = 7,decimal_places=2, null= True, blank=True, default=0.0)
    numReviews = models.IntegerField(null=True, blank=True, default=0)
    #expected_date = models.DateField(default=datetime.today())
    expected_date = models.CharField(max_length=200,null = True, blank = True)
   
    #shipping_date = models.CharField(max_length=200,null = True, blank = True, default=datenow)
    #expected_date = models.CharField(max_length=200,null = True, blank = True)
    website_link = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.product_id)




# class Review(models.Model):
#     product = models.ForeignKey(Product,on_delete = models.SET_NULL,null = True)
#     user = models.ForeignKey(User,on_delete = models.SET_NULL,null = True)
#     name = models.CharField(max_length=200,null = True, blank = True)
#     rating = models.IntegerField(null=True, blank=True, default=0)
#     comment = models.TextField(null=True, blank=True)
#     _id = models.AutoField(primary_key=True, editable=False)

#     def __str__(self):
#         return str(self.rating)
    

