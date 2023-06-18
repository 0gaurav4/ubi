from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class profile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE, blank=True)
    contact=models.BigIntegerField(null=True)
    #collegid=models.BigIntegerField(unique=True, blank=True)
    ppic=models.ImageField(upload_to='pic', default="media\default\person.png")
    address=models.TextField(blank=True)
    city=models.CharField(max_length=20, blank=True)
    state=models.CharField(max_length=20, blank=True)
    pincode=models.IntegerField(default=0)
    update_on=models.DateTimeField(auto_now_add=True, blank=True)
