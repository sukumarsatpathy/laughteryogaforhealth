from django.urls import path
from .import views

urlpatterns = [
    path('', views.testimonial, name='testimonial'),

    path('list/', views.listTestimonials, name='listTestimonials'),
    path('add/', views.addTestimonial, name='addTestimonial'),
    path('edit/<int:pk>', views.editTestimonial, name='editTestimonial'),
]