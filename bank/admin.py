from django.contrib import admin
from .models import Account

# Register your models here.
class AccountAdmin(admin.ModelAdmin):
    readonly_fields = ('balance',)  # make the balance read only in admin page

admin.site.register(Account, AccountAdmin)  # register the model in admin site