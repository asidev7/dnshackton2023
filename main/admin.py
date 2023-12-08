from django.contrib import admin
from main.models import Domaine,NameServer
# Register your models here.

class DomaineAdmin(admin.ModelAdmin):
    list_display = ('nom_domaine', 'date_creation', 'date_expiration', 'status', 'ds_record', 'client')
    search_fields = ('nom_domaine', 'client__username')  # Add fields you want to search by

admin.site.register(Domaine,DomaineAdmin)
admin.site.register(NameServer)