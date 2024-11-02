from django.urls import path
from .views import PartnerList, PartnerDetail

urlpatterns = [
    path('', PartnerList.as_view(), name='partner-list'),
    path('<int:pk>/', PartnerDetail.as_view(), name='partner-detail'),
]
