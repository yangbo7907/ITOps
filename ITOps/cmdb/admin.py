from django.contrib import admin

# Register your models here.

from .models import Brands, Owners, Sla, Fs_usage, Ipaddress, Application, Servers
admin.site.register([Brands, Owners, Sla, Fs_usage, Ipaddress, Application, Servers])

