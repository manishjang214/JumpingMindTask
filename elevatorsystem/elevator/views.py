from rest_framework import viewsets
from .models import Elevator, Request
from .serializers import ElevatorSerializer, RequestSerializer

class ElevatorViewSet(viewsets.ModelViewSet):
    queryset = Elevator.objects.all()
    serializer_class = ElevatorSerializer

class RequestViewSet(viewsets.ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        self.process_request(instance)

    def process_request(self, request):
        elevator = request.elevator
        if elevator.current_floor < request.target_floor:
            elevator.status = 'UP'
        elif elevator.current_floor > request.target_floor:
            elevator.status = 'DOWN'
        else:
            elevator.status = 'STOPPED'
        elevator.current_floor = request.target_floor
        elevator.save()
        request.processed = True
        request.save()
