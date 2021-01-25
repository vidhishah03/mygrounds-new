from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import SignUpView

urlpatterns = [
    path('', views.home_view, name='home'),
<<<<<<< HEAD
    path('signup/', SignUpView.as_view(), name='signup'),    
    path('turfdetails/', views.detailsform_view, name='turfdetails'),
=======
    path('signup/', SignUpView.as_view(), name='signup'),
    path('addturf/',views.addturf_view, name='addturf'),
>>>>>>> 8e9825259cc302673e48f2e79be78839c36b8103
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
