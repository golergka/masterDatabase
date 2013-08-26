from django.db import models

# Edited only by admins
class Service(models.Model):
    url_name = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField()

class Master(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

class MasterService(models.Model):
    master = models.ForeignKey(Master)
    service = models.ForeignKey(Service)
    available = models.BooleanField()
    price = models.PositiveIntegerField(blank=True)
