from django.contrib import admin
from django.contrib.auth.models import Group as BaseGroup
from unfold.admin import ModelAdmin

from data.models import Group

# Unregister group
admin.site.unregister(BaseGroup)


@admin.register(Group)
class GroupAdmin(ModelAdmin):
    pass
