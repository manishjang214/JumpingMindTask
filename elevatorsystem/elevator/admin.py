from django.contrib import admin
from .models import Elevator, Request

# Register your models here.

@admin.register(Elevator)
class ElevatorAdmin(admin.ModelAdmin):
    list_display = ('status', 'current_floor')

@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = ('elevator', 'direction', 'target_floor', 'processed')

    