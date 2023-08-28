from django.urls import path
from . import views

urlpatterns = [
    path('<str:slug>', views.serviceDetail, name='serviceDetail'),
    path('list-categories/', views.serviceCategoryList, name='serviceCategoryList'),
    path('add-category/', views.serviceCategoryAdd, name='serviceCategoryAdd'),
    path('edit-category/<int:pk>/', views.serviceCategoryEdit, name='serviceCategoryEdit'),

    path('list-services/', views.serviceList, name='serviceList'),
    path('add-service/', views.serviceAdd, name='serviceAdd'),
    path('edit-service/<int:pk>/', views.serviceEdit, name='serviceEdit'),
]