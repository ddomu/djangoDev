from .models import F5arp
import django_filters

class ArpFilter(django_filters.FilterSet):
    arp_ip = django_filters.CharFilter(name='arp_ip', lookup_expr = 'contains')
    arp_mac = django_filters.CharFilter(name='arp_mac', lookup_expr = 'contains')
    class Meta:
        model = F5arp
        fields = ['arp_ip', 'arp_mac']
