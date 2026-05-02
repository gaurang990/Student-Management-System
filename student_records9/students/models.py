from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=30,null=True)
    email=models.CharField(max_length=30,null=True)
    college=models.CharField(max_length=30,null=True)
    city=models.CharField(max_length=30,null=True)
    joining_date=models.CharField(max_length=30,null=True)
    total_fee=models.CharField(max_length=30,null=True)
    paid_fee=models.CharField(max_length=30,null=True)
    left_fee=models.CharField(max_length=30,null=True)
    number=models.CharField(max_length=30,null=True)
    technology=models.CharField(max_length=30,null=True)
    image=models.FileField(null=True)
