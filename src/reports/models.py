from django.db import models
from django.urls import reverse
from account.models import Discipline ,Account
from django.utils import timezone
import datetime
import os

shiftchoices=(("Day","Day"),("Night","Night"))

class Wind(models.Model):
   wind_velocity=models.CharField( max_length=20,unique=True ) 
   def __str__(self):
        return str(self.wind_velocity)

class Weather(models.Model):
    weather=models.CharField(max_length=20,unique=True)
    def __str__(self):
        return str(self.weather)

class Cp(models.Model):
    cpno=models.CharField(max_length=10,unique=True)

    def __str__(self):
        return self.cpno       

class Activity(models.Model):
    activity=models.CharField(max_length=30,unique=True)

    def __str__(self):
        return self.activity   
class Area(models.Model):
    area=models.CharField(max_length=30,unique=True)
    def __str__(self):
        return self.area

def set_filename_format(now,instance, filename):
    
    return "{username}-{date}-{microsecond}{extension}".format(
        username=instance.created_by,
        date=str(now.date()),
        microsecond=now.microsecond,
        extension=os.path.splitext(filename)[1],
    )        

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    now = datetime.datetime.now()
    path = "daily/{year}/{month}/{day}/{username}/{filename}".format(
        year=now.year,
        month=now.month,
        day=now.day,
        username=instance.created_by,
        filename=set_filename_format(now,instance, filename),
    )
   

    return path

class DailyReport(models.Model):

    created_by=models.ForeignKey(Account,related_name='created_by',related_query_name='created_by' ,on_delete=models.PROTECT)
    wind_velocity=models.ForeignKey(Wind, blank=True ,null=True,on_delete=models.SET_NULL)
    temp=models.CharField(blank=True, max_length=10)
    weather=models.ForeignKey(Weather, blank=True ,null=True,on_delete=models.SET_NULL)
    datetimestamp= models.DateTimeField(blank=True, default=timezone.now)
    shift=models.CharField(max_length=20,blank=True ,null=True ,choices=shiftchoices ,default='Day')
    updated=models.DateTimeField(auto_now_add=False , auto_now=True)
    status=models.BooleanField(default=True)
    attachment=models.FileField(upload_to=user_directory_path,null=True ,blank=True)

    def __str__(self):
        return str(self.id)
        
    def get_absolute_url(self):
        return reverse('detail_report', kwargs={"pk": self.pk})


class ReportActivity(models.Model):
        reportnumber=models.ForeignKey(DailyReport,blank=True ,null=True,on_delete=models.SET_NULL)      
        activity=models.ForeignKey(Activity,blank=True ,null=True,on_delete=models.SET_NULL)      
        cp=models.ForeignKey(Cp, blank=True ,null=True,on_delete=models.SET_NULL)
        area =models.ForeignKey(Area,blank=True ,null=True,on_delete=models.SET_NULL)
        
        description = models.TextField(blank=True)
        remarks= models.TextField(blank=True)


        def __str__(self):

            return str(self.reportnumber)