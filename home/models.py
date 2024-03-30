from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Details(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,default=None)
    full_name=models.CharField(max_length=100)
    email=models.EmailField(null=False,blank=False)
    mobile_no=models.TextField()
    areain=models.TextField()
    address=models.TextField()
    cv=models.FileField()

class Jobs(models.Model):
    job_head=models.TextField()
    job_location=models.TextField()
    job_qual1=models.TextField()
    job_qual2=models.TextField()
    job_qual3=models.TextField()