from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import SignUpView

urlpatterns = [
    path('', views.home_view, name='home'),
    path('signup/', SignUpView.as_view(), name='signup'),    
    path('turfdetails/', views.detailsform_view, name='turfdetails'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
