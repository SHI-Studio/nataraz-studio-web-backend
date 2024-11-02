from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from .models import Blog
from .serializers import BlogSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from django.core.files.storage import default_storage

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAdminUser]

class FileUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request):
        file = request.FILES.get('upload')
        if file:
            file_name = default_storage.save(file.name, file)
            file_url = default_storage.url(file_name)
            return Response({'url': request.build_absolute_uri(file_url)}, status=201)
        return Response({'error': 'Not uploaded.'}, status=400)
