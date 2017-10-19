from django.db import models

# Create your models here.

class Brands(models.Model):
    brand_id = models.AutoField(primary_key=True)
    brand_name = models.CharField(max_length=50)     #HPE, IBM, VMWARE, etc.
    brand_contact = models.CharField(max_length=250)

class Owners(models.Model):
    owner_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    mobile = models.IntegerField()
    email = models.EmailField()
    team = models.CharField(max_length=50)

class Sla(models.Model):
    sla_id = models.IntegerField(primary_key=True)  # 1,2,3 ...
    response = models.CharField(max_length=50)   # 5X8, 5X9, 7X24, ...

class Fs_usage(models.Model):
    fs_name = models.CharField(max_length=50)   # /, /u01, C: D:
    fs_type = models.CharField(max_length=50)
    server_id = models.IntegerField()     #models.ForeignKey(Servers)  ... not defined error     
    fs_usage = models.IntegerField()     # 70, 80, 95, etc. 
    last_update = models.DateTimeField(auto_now=True)
    
class Ipaddress(models.Model):
    ip_id = models.AutoField(primary_key=True)
    ipaddress = models.GenericIPAddressField()
    netmask = models.GenericIPAddressField()
    gateway = models.GenericIPAddressField()
    dns1 = models.GenericIPAddressField()
    dns2 = models.GenericIPAddressField()
    last_update = models.DateTimeField(auto_now=True)
    
class Application(models.Model):
    app_id = models.AutoField(primary_key=True)
    app_type = models.CharField(max_length=50)    #DB, WEB, SAP ... etc.

class Servers(models.Model):
    STATUS_CHOICES = (
        (u'IN_PRD', u'In Production'),
        (u'NOT_PRD', u'Not In Production'),
    )
    SERVTYPE_CHOICES = (
        (u'VM', u'Virtual Machine'),
        (u'HW', u'Hardware'),
    )
    server_id = models.AutoField(primary_key=True)
    fqdn = models.CharField(max_length=150)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)  #IN_PRD, NOT_PRD
    server_type = models.CharField(max_length=10, choices=SERVTYPE_CHOICES)  #VM, HW
    nCPU = models.IntegerField()     #CPU number
    CPU_t = models.CharField(max_length=10)        #X86_64, X86, POWER, etc.
    nRAM = models.IntegerField()     # 4, 6, 8 ...
    ip_id = models.ForeignKey(Ipaddress)  
    os_type = models.CharField(max_length=50)    #WINDOWS, RHEL, SLES, UBUNTU, AIX, HP-UX
    os_ver = models.CharField(max_length=50)     
    sla_id = models.ForeignKey(Sla)
    brand_id = models.ForeignKey(Brands)
    owner_id = models.ForeignKey(Owners)
    backup_owner_id = models.IntegerField()
    app_id = models.ForeignKey(Application)    
