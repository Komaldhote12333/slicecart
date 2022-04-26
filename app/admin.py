from django.contrib import admin
from .models import Idcard
from django.db import models



class show(admin.ModelAdmin):
    list_display = ['name','father','branch','valid_up','DOB','roll']
# Register your models here.
admin.site.register(Idcard,show)