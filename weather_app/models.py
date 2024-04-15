from django.db import models
from django.utils import timezone
class weather(models.Model):
    city = models.CharField(max_length=1000)
    country_code = models.CharField(max_length=1000)
    coordinate = models.CharField(max_length=1000)
    temp = models.CharField(max_length=1000)
    pressure = models.CharField(max_length=1000)
    humidity = models.CharField(max_length=1000)
    timestamp = models.DateTimeField(default=timezone.now)
                                     
# Create your models here.
