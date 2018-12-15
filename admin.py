from django.contrib import admin

# Register your models here.
from .models import F5vcmp, F5arp
from trunk.models import Site

class F5vcmpAdmin(admin.ModelAdmin):
    list_display = ('site','vcmp_name', 'vcmp_ip','env_type', 'tm_type',  
                    )
    #ordering = ['id']

class F5arpAdmin(admin.ModelAdmin):
    list_display = ('id', 'site', 'vcmp_name', 'arp_ip', 'arp_mac', 'arp_vlan', 'arp_status', 'updated', 
                    )
    #ordering = ['created_date']


admin.site.register(F5vcmp,F5vcmpAdmin)
admin.site.register(F5arp, F5arpAdmin)
