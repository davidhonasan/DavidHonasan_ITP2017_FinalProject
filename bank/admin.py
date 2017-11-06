from django.contrib import admin
from .models import Account
from django.contrib.auth.models import User

# Register your models here.
class AccountAdmin(admin.ModelAdmin):
    readonly_fields = ('balance',)

admin.site.register(Account, AccountAdmin)