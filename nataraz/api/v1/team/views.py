from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from .models import Member, ExtraData
from .serializers import MemberSerializer, ExtraDataSerializer

class MemberList(generics.ListCreateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    permission_classes = [IsAdminUser]

class MemberDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    permission_classes = [IsAdminUser]

class ExtraDataList(generics.ListCreateAPIView):
    queryset = ExtraData.objects.all()
    serializer_class = ExtraDataSerializer
    permission_classes = [IsAdminUser]

class ExtraDataDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ExtraData.objects.all()
    serializer_class = ExtraDataSerializer
    permission_classes = [IsAdminUser]
