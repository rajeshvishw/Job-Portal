from django.contrib import admin

from .models import *

admin.site.register(UserMaster)
admin.site.register(candidate)
admin.site.register(company)