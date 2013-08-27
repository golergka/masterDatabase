from django.db import models

# Edited only by admins
class Service(models.Model):
    url_name = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __unicode__(self):
        return self.name

class Master(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __unicode__(self):
        return self.name

class MasterService(models.Model):
    master = models.ForeignKey(Master)
    service = models.ForeignKey(Service)
    price = models.PositiveIntegerField(blank=True)