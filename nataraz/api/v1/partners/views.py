from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from .models import Partner
from .serializers import PartnerSerializer

class PartnerList(generics.ListCreateAPIView):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer
    permission_classes = [IsAdminUser]

class PartnerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer
    permission_classes = [IsAdminUser]
