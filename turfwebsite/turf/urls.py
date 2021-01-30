from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import SignUpView, myaccountview, passwordchangeview, editturfview
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('signup/', SignUpView.as_view(), name='signup'),    
    path('turfdetails/', views.detailsform_view, name='turfdetails'),
    path('display/', views.show_turf, name = "display"),
    path('myaccount/', myaccountview.as_view(), name='myaccount'),
    path('contactus/', views.show_contacts, name = "contactus"),
    path('password/',passwordchangeview.as_view(), name = 'password'),
    path('gallery/',views.feedbackview, name = 'gallery'),
    path('myturfs/',views.show_myturfs, name = "myturfs"),
    path('book/',views.bookingview,name= "book"),
    path('editturf/', views.editturfview, name='editturf'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
