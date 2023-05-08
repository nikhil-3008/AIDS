from django.contrib import admin
from django.urls import path,include
from .views import *
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Home,name='Home'),
    path('about/',about,name='about'),
    path('papers/',papers,name='papers'),
    path('login/',Login,name='login'),
    path('logout/',Logout,name='logout'),
    path('OtpVerification/',OtpVerification,name='OtpVerification'),
    path('study_material/',study_material,name='study_material'),
    path('pdfviewer/',pdfviewer,name='pdfviewer'),
    path('study_material/pdfviewer/',pdfviewer,name='pdfviewer'),
    path('login/signup/',signup,name='signup'),
    path('signup/login/',Login,name='login'),
    path('signup/',signup,name='signup'),]+ static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])