from django.contrib import admin
from masterCollection.models import Master, Service, MasterService

# Custom user admin
# https://docs.djangoproject.com/en/dev/topics/auth/customizing/#extending-the-existing-user-model

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

admin.site.register(Service)

class ServiceInline(admin.StackedInline):
    model = MasterService
    extra = 3

    def has_change_permission(self, request, obj=None):
        if (obj==None):
            return True
        else:
            return obj.master.user == request.user

class MasterAdmin(admin.ModelAdmin):
    inlines = [ServiceInline]
    list_display = ('name', 'description')

    def queryset(self, request):
        qs = super(MasterAdmin, self).queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)

    def has_change_permission(self, request, obj=None):
        if (obj==None or request.user.is_superuser):
            return True
        else:
            return obj.user == request.user

    def get_form(self, request, obj=None, **kwargs):

        if self.exclude == None:
            self.exclude = []

        if not request.user.is_superuser:
            self.exclude.append('user')
            self.exclude.append('published')

        return super(MasterAdmin, self).get_form(request, obj, **kwargs)

admin.site.register(Master, MasterAdmin)

class MasterInline(admin.StackedInline):
    model = Master
    can_delete = True

class UserAdmin(UserAdmin):
    inlines = (MasterInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)