from django.db import models

class Idcard(models.Model):
    name = models.CharField(max_length=23)
    father = models.CharField(max_length=23)
    branch = models.CharField(max_length=23)
    valid_up = models.CharField(max_length=23)
    DOB =models.DateField(default='08/07/2004')
    roll=models.CharField(max_length=34)
    img =models.ImageField(upload_to='image',default='images.png')
# Create your models here.
