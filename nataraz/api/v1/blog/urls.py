from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BlogViewSet, FileUploadView

router = DefaultRouter()
router.register(r'', BlogViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('upload/', FileUploadView.as_view(), name='file-upload'),
]
