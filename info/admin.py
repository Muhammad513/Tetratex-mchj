from django.contrib import admin
from .models import*
# Register your models here.
class PositionAdmin(admin.ModelAdmin):
    list_display=('id',"position_name")

class StaffAdmin(admin.ModelAdmin):
    list_display=('id',"first_name",'last_name',"stir_num",'pasport','birthday','position')
    list_display_links=('id',"first_name")


class TabelAdmin(admin.ModelAdmin):
    list_display=('staff','date','public',)
    list_display_links=("staff",)


admin.site.register(Sidebar)
admin.site.register(Submenu)

admin.site.register(Position,PositionAdmin)
admin.site.register(Staff,StaffAdmin)
admin.site.register(Tabel,TabelAdmin)