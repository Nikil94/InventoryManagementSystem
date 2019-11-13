from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)

    def __unicode__(self):
        return self.user

class Products(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, blank=True, null=True)
    productid = models.IntegerField(max_length=10, unique=True, blank=True)
    productname = models.CharField(max_length=255, blank=True)
    vendor = models.CharField(max_length=100, blank=True)
    mrp = models.IntegerField(max_length=10, blank=True)
    batchdate = models.DateTimeField(auto_now_add=True)
    batchnumber = models.IntegerField(max_length=1000, blank=True)
    quantity = models.IntegerField(max_length=1000, blank=True)
    status_approved = models.CharField(max_length=100, default='Pending')

