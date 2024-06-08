from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('',views.home,name='home'),
    path('home/',views.home,name='home'),
    path('404/',views.custom404,name='custom404'),
    path('d/<slug>',views.fileDownload,name='download'),
]
