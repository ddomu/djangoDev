from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^arp/$', views.arp, name='arp'),
    url(r'^subnet/$', views.subnet, name='subnet'),
    url(r'^$', views.index, name='index'),

	]