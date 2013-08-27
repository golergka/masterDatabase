from django.http import HttpResponse
from django.template import RequestContext, loader

from masterCollection.models import Master

def index(request):
    master_list = Master.objects.iterator()
    template = loader.get_template('masterCollection/index.html')
    context = RequestContext(
        request,
        {
            'master_list': master_list
        }
    )

    return HttpResponse(template.render(context))

def master(request, master_id):
    return HttpResponse("TODO master view %s" % master_id)
