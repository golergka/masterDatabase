from django.db import models

# Edited only by admins
class Service(models.Model):
    url_name = models.SlugField(max_length=50, primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __unicode__(self):
        return self.name

class Master(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    email = models.EmailField(max_length=254, unique=True)
    services = models.ManyToManyField(Service, through='MasterService')

    # def get_all_services(self):
    #     result = []
    #     for service_type in Service.objects.iterator():
    #         found = False
    #
    #         for master_service in self.masterservice_set:
    #             if master_service == service_type:
    #                 result.append(master_service)
    #                 found = True
    #                 break
    #
    #         if not found:
    #             result.append()

    def __unicode__(self):
        return self.name

class MasterService(models.Model):
    master = models.ForeignKey(Master)
    service = models.ForeignKey(Service)

    price = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        unique_together=("master", "service")