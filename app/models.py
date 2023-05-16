from django.db import models

# Create your models here.
class School(models.Model):
    Sname=models.CharField(max_length=100)
    Sid=models.IntegerField(primary_key=True)
    # Saddress=models.TextField(max_length=200)