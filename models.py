from django.db import models
from django.forms import ModelForm
from django.utils import timezone
from django.contrib.auth.models import User    
from django.core.validators import MaxValueValidator
from django.db import models
from trunk.models import Site
# Create your models here.

# table f5vcmp.tbl  
class F5vcmp(models.Model): 
    site   = models.ForeignKey('trunk.Site',on_delete=models.CASCADE)
    vcmp_name = models.CharField( max_length = 100 ,null = False)
    vcmp_ip  =  models.GenericIPAddressField(blank=False,)
    env_type  = models.CharField( max_length = 10  ,null = False)  # Prod or Test 
    tm_type  = models.CharField( max_length = 10  ,null = False)  # LTM or GTM 
    def __str__(self):
        return self.vcmp_name


class F5arp(models.Model): 
    site    = models.ForeignKey('trunk.Site',on_delete=models.CASCADE)
    vcmp_name    = models.ForeignKey('F5vcmp',on_delete=models.CASCADE)
    arp_ip  =  models.GenericIPAddressField(blank=False,)
    arp_mac  = models.CharField( max_length = 20  ,null = False)
    arp_vlan = models.CharField( max_length = 100 ,null = True)
    arp_status  = models.CharField( max_length = 10  ,null = False)  # Resolved | Incomplete
    updated    =  models.DateTimeField(blank = True, null = True)
    def update_time(self): 
        self.updated = timezone.now() 
    def __str__(self):
        return self.arp_ip


