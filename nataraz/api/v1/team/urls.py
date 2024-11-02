from django.urls import path
from .views import MemberList, MemberDetail, ExtraDataList, ExtraDataDetail

urlpatterns = [
    
    path('members/', MemberList.as_view(), name='member-list'),
    path('members/<int:pk>/', MemberDetail.as_view(), name='member-detail'),
    path('extradata/', ExtraDataList.as_view(), name='extra-data-list'),
    path('extradata/<int:pk>/', ExtraDataDetail.as_view(), name='extra-data-detail'),
]
