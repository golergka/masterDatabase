from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from masterCollection.models import Master, Service, MasterService

class IndexView(generic.ListView):
    template_name = 'masterCollection/index.html'
    context_object_name = 'master_list'

    def search_string(self):
        return self.request.GET.get('search_string')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['search_string'] = self.search_string()
        return context

    def get_queryset(self):

        lookups = { 'published' : 'True' }
        search_string = self.search_string()
        if not search_string == None:
            lookups['name__icontains'] = search_string

        print lookups

        return Master.objects.filter(**lookups)

class MasterView(generic.DetailView):
    model = Master
    template_name = 'masterCollection/master.html'