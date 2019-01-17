from django.db import models
import datetime

class UserIP(models.Model):
    ip_address = models.CharField(max_length=255)
    host_name = models.CharField(max_length=255)
    first_visit = models.DateTimeField(default=datetime.datetime.now())
    last_visit = models.DateTimeField()
    number_requests = models.IntegerField(default=1)
