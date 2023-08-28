from django.urls import path
from .import views

urlpatterns = [
    path('', views.event, name='event'),
    path('<str:slug>', views.eventDetail, name='eventDetail'),

    path('list/', views.listEvent, name='listEvents'),
    path('add/', views.addEvent, name='addEvent'),
    path('edit/<str:slug>', views.editEvent, name='editEvent'),
]