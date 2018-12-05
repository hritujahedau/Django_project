# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Department(models.Model):
    id = models.AutoField(primary_key=True)
    departmentId = models.CharField(max_length=200)
    departmentName = models.CharField(max_length=200)
    
class Course(models.Model):
    id = models.AutoField(primary_key=True)
    courseId  = models.CharField(max_length=200)
    courseName = models.CharField(max_length=200)
    departmentName = models.ForeignKey(Department, on_delete=models.CASCADE)
