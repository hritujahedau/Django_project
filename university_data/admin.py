# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Department
from .models import Course

admin.site.register(Department)
admin.site.register(Course)


# Register your models here.
