from re import search
from django.contrib import admin

from contacts.models import contacts

# Register your models here.
class ContactsAdmin(admin.ModelAdmin):
    list_display=('id','firstname','lastname','car_title', 'city', 'state','email','create_date')
    list_display_links=('id','firstname','email','car_title')
    list_filter=('firstname','car_title')
    list_per_page=25
    search_fields=('id','firstname','lastname','car_title')



admin.site.register(contacts,ContactsAdmin)