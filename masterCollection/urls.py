from django.conf.urls import patterns, url

from masterCollection import views

urlpatterns = patterns('',
    url(r'^$',                           views.IndexView.as_view(),  name='index'),
    url(r'^master/(?P<pk>\d+)/$',        views.MasterView.as_view(), name='master'),
)