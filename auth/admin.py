from django.contrib import admin
from auth.models import InviteCode


@admin.register(InviteCode)
class InviteCodeAdmin(admin.ModelAdmin):
    pass