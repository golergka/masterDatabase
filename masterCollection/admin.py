from django.contrib import admin
from masterCollection.models import Master, Service, MasterService

admin.site.register(Service)

class ServiceInline(admin.StackedInline):
    model = MasterService
    extra = 3

class MasterAdmin(admin.ModelAdmin):
    fields = ['name', 'description']
    inlines = [ServiceInline]

admin.site.register(Master, MasterAdmin)