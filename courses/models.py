from django.db import models

class Activity_Period(models.Model):
    e_id= models.CharField(max_length=15)
    real_name= models.CharField(max_length=30)
    tz= models.CharField(max_length=30)
    activity_periods=models.TextField()
    
    # to give the course object name in django
    def __str__(self):
        return self.e_id
