from django.db import models
from django.contrib.auth.models import User

# Edited only by admins
class Service(models.Model):
    url_name = models.SlugField(max_length=50, primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __unicode__(self):
        return self.name

class Master(models.Model):
    name        = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    email       = models.EmailField(max_length=254, unique=True)
    services    = models.ManyToManyField(Service, through='MasterService')
    user        = models.OneToOneField(User, null=True)
    published   = models.BooleanField(default=False)
    address     = models.CharField(max_length=1000, blank=True)

    def __unicode__(self):
        return self.name

class MasterService(models.Model):
    master = models.ForeignKey(Master)
    service = models.ForeignKey(Service)

    price = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        unique_together=("master", "service")