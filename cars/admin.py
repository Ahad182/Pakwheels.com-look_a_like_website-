
from django.utils.html import format_html
from django.contrib import admin

from cars.models import CarTeam

# Register your models here.
class carAdmin(admin.ModelAdmin):
    def photo(self,object):
        return format_html('<img src="{}" width="40px" style="border-radius:50px"/>'.format(object.car_photo.url))
        
    list_display=('id','photo','car_name','city','year','is_featured')
    list_display_links=('id','car_name','city')
    list_filter=('car_name','city','year','is_featured')
    search_fields=('id','car_name','city','year','is_featured')
    list_editable=('is_featured','year')


admin.site.register( CarTeam,carAdmin)
