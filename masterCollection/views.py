from django.http import Http404
from django.shortcuts import render, get_object_or_404

from masterCollection.models import Master, Service, MasterService

def index(request):
    master_list = Master.objects.iterator()
    context = { 'master_list': master_list }
    return render(request, 'masterCollection/index.html', context)

def master(request, master_id):
    master = get_object_or_404(Master, pk = master_id)
    return render(request, 'masterCollection/master.html', { 'master': master })
