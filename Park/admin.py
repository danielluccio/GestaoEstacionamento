from django.contrib import admin
from .models import ParkingRecord, ParkingSpot

@admin.register(ParkingSpot)
class ParkingSpotAdmin(admin.ModelAdmin):
    list_display = ('spot_number', 'is_occupied')
    search_fields  = ('spot_number', 'is_occupied')

@admin.register(ParkingRecord)
class ParkingRecordAdmin(admin.ModelAdmin):
    list_display = ('vehicle', 'parking_spot', 'entry_time')
    search_fields  = ('vehicle', 'parking_spot', 'entry_time')


