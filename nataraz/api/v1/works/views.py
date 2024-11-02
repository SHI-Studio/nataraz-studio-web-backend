from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from .models import Work
from .serializers import WorkSerializer

class WorkViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        raise PermissionDenied("You are not authorized for this operation.")

    def update(self, request, *args, **kwargs):
        raise PermissionDenied("You are not authorized for this operation.")

    def destroy(self, request, *args, **kwargs):
        raise PermissionDenied("You are not authorized for this operation.")
