from django.contrib import admin
from .models import Vehicle, VehicleType


class VehicleAdmin(admin.ModelAdmin):
    list_display = ('vehicle_type', 'license_plate', 'brand')
    search_fields = ('vehicle_type', 'license_plate', 'brand')


class VehicleTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')

admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(VehicleType, VehicleTypeAdmin)