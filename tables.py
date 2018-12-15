import django_tables2 as tables
from .models import F5arp

class F5arpTable(tables.Table):
    class Meta:
        model = F5arp
        template_name = 'django_tables2/semantic.html'