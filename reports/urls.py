from django.urls import path
from .import views

urlpatterns = [
    path('cfd/', views.contactData, name='cfd'),
    path('cfd/<int:pk>', views.contactDataView, name='cfdView'),
    path('invtd/', views.inviteData, name='invtd'),
    path('invtd/<int:pk>', views.inviteDataView, name='invtdView'),
    path('nwsld/', views.newsletterData, name='nwsld'),
]