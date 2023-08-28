from django.urls import path
from django.shortcuts import redirect
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about-ashwin-and-deepika/', views.aboutTrainer, name='aboutTrainer'),

    path('contact/', views.contact, name='contact'),
    path('subscribe/', views.subscribe, name='subscribe'),

    path('adblockList/', views.adblockList, name='adblockList'),
    path('adblockAdd/', views.adblockAdd, name='adblockAdd'),
    path('adblockEdit/<int:pk>/', views.adblockEdit, name='adblockEdit'),

    path('journalList/', views.journalList, name='journalList'),
    path('journalAdd/', views.journalAdd, name='journalAdd'),
    path('journalEdit/<int:pk>/', views.journalEdit, name='journalEdit'),

    path('bannerList/', views.bannerList, name='bannerList'),
    path('bannerEdit/<int:pk>', views.bannerEdit, name='bannerEdit'),

    path('bannerImageList/', views.bannerImageList, name='bannerImageList'),
    path('bannerImageAdd/', views.bannerImageAdd, name='bannerImageAdd'),
    path('bannerImageEdit/<int:pk>', views.bannerImageEdit, name='bannerImageEdit'),

    #Settings Edit
    path('contactPageEdit/', views.contactPageEdit, name='contactPageEdit'),
    path('copyrightPageEdit/', views.copyrightPageEdit, name='copyrightPageEdit'),
    path('webSettingsEdit/', views.webSettingsEdit, name='webSettingsEdit'),

    # Term Pages
    path('list-term-pages/', views.ListTermPage, name='ListTermPage'),
    path('pages/<str:slug>/', views.termPage, name='termPage'),
    path('editPage/<str:slug>', views.editTermPage, name='editTermPage'),

    path('login/', lambda request: redirect('login', permanent=True)), # /accounts -> redirects to Frontend Login

    # About Pages
    path('<str:slug>/', views.aboutDetailPage, name='aboutDetailPage'),
]