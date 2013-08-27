from django.conf.urls import patterns, url

from masterCollection import views

urlpatterns = patterns('',
    url(r'^$',                             views.index,  name='index'),
    url(r'^master/(?P<master_id>\d+)/$',   views.master, name='master'),
)