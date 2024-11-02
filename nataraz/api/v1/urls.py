from django.urls import path, include
# from . import general
from .general import views as generalView
from .services import views as servicesView
from .procces import views as proccesView
from .about import views as aboutView



urlpatterns = [
    path('general/', generalView.MediaList.as_view(), name='media-list'),
    path('services/', servicesView.ServiceList.as_view(), name='service-list'),
    path('services/<int:pk>/', servicesView.ServiceDetail.as_view(), name='service-detail'),
    path('services/tags/', servicesView.TagList.as_view(), name='tag-list'),
    path('services/tags/<int:pk>/', servicesView.TagDetail.as_view(), name='tag-detail'),
    path('process/', proccesView.ProcessList.as_view(), name='process-list'),
    path('process/<int:pk>/', proccesView.ProcessDetail.as_view(), name='process-detail'),
    path('about/', aboutView.AboutDetail.as_view(), name='about-detail'),
    path('team/', include('api.v1.team.urls')),
    path('partners/', include('api.v1.partners.urls')),
    path('testimonials/', include('api.v1.testimonials.urls')),
    path('works/', include('api.v1.works.urls')),
    path('blog/', include('api.v1.blog.urls')),

]
