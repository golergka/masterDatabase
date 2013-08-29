from django.contrib import admin
from masterCollection.models import Master, Service, MasterService

admin.site.register(Service)

class ServiceInline(admin.StackedInline):
    model = MasterService
    extra = 3

class MasterAdmin(admin.ModelAdmin):
    fields = ['name', 'description', 'email', 'user']
    inlines = [ServiceInline]
    list_display = ('name', 'description')

admin.site.register(Master, MasterAdmin)

# Custom user admin
# https://docs.djangoproject.com/en/dev/topics/auth/customizing/#extending-the-existing-user-model

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

class MasterInline(admin.StackedInline):
    model = Master
    can_delete = True

class UserAdmin(UserAdmin):
    inlines = (MasterInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)