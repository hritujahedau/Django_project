# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class Location(models.Model):    
    id = models.AutoField(primary_key=True)
    state = models.CharField(max_length=200)
    district = models.CharField(max_length=200)
    country = models.CharField(max_length=200)


class User(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=200) 
    last_name = models.CharField(max_length=200)  
    profile_pic_url = models.CharField(max_length=200)
    location = models.ForeignKey(Location, on_delete=None)
    mobile_number = models.CharField(max_length=10)  
       

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    time = models.TimeField(blank=True, null=True)
    updated_time = models.TimeField(blank=True, null=True)
    user = models.ForeignKey(User) 
    is_deleted = models.BooleanField(default=False)
    


class DataInfo(models.Model):
    id = models.AutoField(primary_key=True)
    data_info_type = models.CharField(max_length=200)
    value = models.CharField(max_length=200)
    post = models.ForeignKey(Post, on_delete=None)
    is_deleted = models.BooleanField(default=False)
    deleted_time = models.TimeField(blank=True, null=True)


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User)  
    post = models.ForeignKey(Post)  


class PostLikeDisLikeByPeople(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User)  
    post = models.ForeignKey(Post)  
    _type = models.CharField(max_length=200)   # "like or dislike"
