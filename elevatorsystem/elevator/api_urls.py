from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import (
    ElevatorSystemViewSet,
    ElevatorViewSet,
    ElevatorRequestViewSet,
    TimeIncrementViewSet,
)

# Create a SimpleRouter instance
router = SimpleRouter()

# Register your main viewsets with the router
router.register(r"elevator-system", ElevatorSystemViewSet, basename="elevator-system")
router.register(r"elevator", ElevatorViewSet, basename="elevator")
router.register(r"elevator-request", ElevatorRequestViewSet, basename="elevator-request")

# Define nested routes for ElevatorSystemViewSet
nested_router = SimpleRouter()
nested_router.register(r'elevator', ElevatorViewSet, basename='elevator')
nested_router.register(r'request', ElevatorRequestViewSet, basename='request')

# Define urlpatterns
urlpatterns = [
    # Add your other URL patterns here if needed
    path("time-increment", TimeIncrementViewSet.as_view({"post": "post"})),
]

# Include main router.urls in urlpatterns
urlpatterns += router.urls

# Include nested_router.urls under a nested path
urlpatterns += [
    path('api/', include(router.urls)),
    path('api/<int:elevator_system_pk>/', include(nested_router.urls)),
]
