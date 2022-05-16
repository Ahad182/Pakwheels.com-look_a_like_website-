from django.contrib import admin
from pages.models import Team
from django.utils.html import format_html

# Register your models here.

class TeamAdmin(admin.ModelAdmin):

    def photo(self, object):
        return format_html('<img src="{}" width="40px" style="border-radius:50px" />'.format(object.img.url))
        
    list_display=('id','f_name','l_name','email','photo','Designation','date')
    list_display_links=('id','f_name')
    list_filter=('Designation',)
    search_fields=('f_name','id','Designation')
    


admin.site.register(Team, TeamAdmin)


