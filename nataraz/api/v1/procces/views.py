from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from .models import Process
from .serializers import ProcessSerializer

class ProcessList(generics.ListCreateAPIView):
    queryset = Process.objects.all()
    serializer_class = ProcessSerializer
    permission_classes = [IsAdminUser]

    def post(self, request, *args, **kwargs):
        return Response({'detail': 'This API can be used for reading only.'}, status=403)

class ProcessDetail(generics.RetrieveAPIView):
    queryset = Process.objects.all()
    serializer_class = ProcessSerializer
    permission_classes = [IsAdminUser]
