from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from .models import Media
from .serializers import MediaSerializer

class MediaList(generics.ListAPIView):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer
    permission_classes = [IsAdminUser]

    def post(self, request, *args, **kwargs):
        return Response({'detail': 'This API can be used for reading only.'}, status=403)


