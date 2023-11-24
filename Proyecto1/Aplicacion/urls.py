from django.urls import path, include
from .views import *
from . import views

urlpatterns = [
    path ("",index , name="index"),
    path('registro/', registro, name='registro'),
    path('home/', home, name='home'),
    path('about_me/', about_me, name='about_me'),
    path('post/', post, name='post'),
    path('admin/', admin_view, name='admin'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    
]
