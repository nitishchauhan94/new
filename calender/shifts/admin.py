from django.contrib import admin

# Register your models here.
from models import shifts

class ShiftAdmin(admin.ModelAdmin):
    list_display = ["date","Day","Morning","Evening","General","Planned","Comp_off","Leave"]


admin.site.register(shifts,ShiftAdmin)
