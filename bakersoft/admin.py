from django.contrib import admin
from .models import Produkt


class ProduktAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'kategorie', 'verfugbar')
    list_per_page = 50
    search_fields = ('name', 'id', 'kategorie')


admin.site.register(Produkt, ProduktAdmin)

