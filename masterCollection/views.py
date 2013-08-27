from django.http import HttpResponse

def index(request):
    return HttpResponse("TODO index")

def master(request, master_id):
    return HttpResponse("TODO master view %s" % master_id)
