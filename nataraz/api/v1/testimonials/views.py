from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from .models import Testimonial
from .serializers import TestimonialSerializer

class TestimonialList(generics.ListCreateAPIView):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer
    permission_classes = [IsAdminUser]

class TestimonialDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer
    permission_classes = [IsAdminUser]
