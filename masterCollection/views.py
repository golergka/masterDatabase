from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from masterCollection.models import Master, Service, MasterService

class IndexView(generic.ListView):
    template_name = 'masterCollection/index.html'
    context_object_name = 'master_list'

    def get_queryset(self):
        return Master.objects.iterator()

class MasterView(generic.DetailView):
    model = Master
    template_name = 'masterCollection/master.html'