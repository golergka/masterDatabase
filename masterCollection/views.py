from django.http import HttpResponse
from django.shortcuts import render

from masterCollection.models import Master

def index(request):
    master_list = Master.objects.iterator()
    context = { 'master_list': master_list }
    return render(request, 'masterCollection/index.html', context)

def master(request, master_id):
    return HttpResponse("TODO master view %s" % master_id)
