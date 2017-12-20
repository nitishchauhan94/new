from django.contrib import admin

# Register your models here.
from .models import Shift

class ShiftModelAdmin(admin.ModelAdmin):
     list_display = ["Date","Day","Morning","Evening","General"]
     list_filter = ["Date","Day","Morning","Evening","General"]
     search_fields = ["Date","Day","Morning","Evening","General"]
     class Meta:
         model  = Shift


admin.site.register(Shift,ShiftModelAdmin)
