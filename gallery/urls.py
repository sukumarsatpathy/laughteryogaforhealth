from django.urls import path
from django.shortcuts import redirect
from .import views

urlpatterns = [
    path('', lambda request: redirect('pictureCL', permanent=True)), # /gallery -> redirects to photo caegory list page
    path('picture/', views.pictureCL, name='pictureCL'),
    path('picture/<str:slug>', views.pictureDetail, name='pictureDetail'),

    path('pcatList/', views.pcatList, name='pcatList'),
    path('pcatAdd/', views.pcatAdd, name='pcatAdd'),
    path('pcatEdit/<str:slug>', views.pcatEdit, name='pcatEdit'),

    path('photoList/', views.photoList, name='photoList'),
    path('photoAdd/', views.photoAdd, name='photoAdd'),
    path('photoEdit/<int:pk>', views.photoEdit, name='photoEdit'),

    path('video/', views.vdoList, name='vdoList'),
    path('video/<str:slug>', views.vdoDetail, name='vdoDetail'),

    path('vcatList/', views.vcatList, name='vcatList'),
    path('vcatAdd/', views.vcatAdd, name='vcatAdd'),
    path('vcatEdit/<str:slug>', views.vcatEdit, name='vcatEdit'),

    path('videoList/', views.videoList, name='videoList'),
    path('videoAdd/', views.videoAdd, name='videoAdd'),
    path('videoEdit/<int:pk>', views.videoEdit, name='videoEdit'),
]