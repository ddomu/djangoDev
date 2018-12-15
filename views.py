# -*- coding: utf-8 -*-
# Create your views here.
from django.shortcuts import render
from django_tables2 import RequestConfig
from .models import F5arp
from .tables import F5arpTable
from .filters import ArpFilter 
# Filtering data in your table 
#from django_filters.views import FilterView
#from django_tables2.views import SingleTableMixin

def index(request):
    return render(request, 'f5app/index.html')

# /f5app/arp/ -------------------
def arp(request):
    arp = F5arp.objects.all()
    table = F5arpTable(arp)
    RequestConfig(request).configure(table) # get the regular arp table as table form

    arp_filter = ArpFilter(request.GET, queryset = arp)
    arp_t = F5arpTable(arp_filter.qs) 
    RequestConfig(request).configure(arp_t)  # Need for Page and... 
    return render(request, 'f5app/arp_search.html', {'arp_t':arp_t, 'filter': arp_filter, })


# /f5app/subnet/ ----------

def subnet(request):
    return render(request, 'f5app/index.html')



""" Old code 
def arp_list(request):
    table = F5arpTable(F5arp.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'f5app/arp_list.html', {'arps':table})
"""