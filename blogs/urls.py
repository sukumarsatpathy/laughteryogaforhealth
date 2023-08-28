from django.urls import path
from .import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('<str:slug>', views.blogDetail, name='blogDetail'),

    path('list/', views.listBlog, name='listBlogs'),
    path('add/', views.addBlog, name='addBlog'),
    path('edit/<str:slug>', views.editBlog, name='editBlog'),
]