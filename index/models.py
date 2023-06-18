from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model

# Create your models here.
class Category(models.Model):
    cat_name=models.CharField(max_length=250)
    cover_pic=models.ImageField(upload_to="cpics")
    description=models.TextField()
    added_on=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cat_name

class Services(models.Model):
    name=models.CharField(max_length=50)
    seller=models.ForeignKey(User,on_delete=models.CASCADE)
    desc=models.TextField()
    cate=models.ForeignKey(Category,on_delete=models.CASCADE)
    price=models.IntegerField()
    image=models.ImageField(upload_to="pics")

    def __str__(self):
        return self.name

class cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Services,on_delete=models.CASCADE)
    qty=models.IntegerField()
    status=models.BooleanField(default=False)
    added_on=models.DateTimeField(auto_now_add=True,null=True)
    updated_on=models.DateTimeField(auto_now=True,null=True)

class Order(models.Model):
    cust_id = models.ForeignKey(User,on_delete=models.CASCADE)
    cart_ids = models.CharField(max_length=250)
    product_ids = models.CharField(max_length=250)
    invoice_id = models.CharField(max_length=250)
    status = models.BooleanField(default=False)
    processed_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cust_id.username

class video_lecture(models.Model):
    name=models.CharField(max_length=250)
    subject=models.TextField()
    teacher=models.CharField(max_length=250)
    video=models.FileField()
    description=models.TextField()

    def __str__(self):
        return self.name
