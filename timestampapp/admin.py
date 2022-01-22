from django.contrib import admin
from .models import UuidTimeStamp

# Register your models here.

class UuidTimeStampAdmin(admin.ModelAdmin):
    readonly_fields=('uuid_code', 'timestamp_str')


admin.site.register(UuidTimeStamp, UuidTimeStampAdmin)
