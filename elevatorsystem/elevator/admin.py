from django.contrib import admin
from elevator.models import ElevatorSystem, Elevator, ElevatorRequest


class ElevatorSystemAdmin(admin.ModelAdmin):
    list_display = ("name", "no_of_floors")


class ElevatorAdmin(admin.ModelAdmin):
    list_display = (
        "elevator_system",
        "status",
        "current_floor",
        "destination_floor",
        "status",
    )


class ElevatorRequestAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "from_floor",
        "to_floor",
        "status",
    )


admin.site.register(ElevatorSystem, ElevatorSystemAdmin)
admin.site.register(Elevator, ElevatorAdmin)
admin.site.register(ElevatorRequest, ElevatorRequestAdmin)