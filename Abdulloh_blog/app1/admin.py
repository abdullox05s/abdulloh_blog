from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import *

admin.site.register([Category,Tags,Author,Blog,Comment])