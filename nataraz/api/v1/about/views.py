from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from .models import About
from .serializers import AboutSerializer

class AboutDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer
    permission_classes = [IsAdminUser]

    def get_object(self):
        obj, created = About.objects.get_or_create(title="About")
        return obj

    def destroy(self, request, *args, **kwargs):
        return Response({"detail": "The About object cannot be deleted."}, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, *args, **kwargs):
        return Response({"detail": "A new About object cannot be created. There can only be one."}, status=status.HTTP_400_BAD_REQUEST)
