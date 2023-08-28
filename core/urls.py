from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('secure-login/owner=lyi~type=superAdmin/', admin.site.urls),
    path('admin/', lambda request: redirect('login', permanent=True)), # /accounts -> redirects to Frontend Login
    path('accounts/', include('accounts.urls')),
    path('testimonials/', include('testimonials.urls')),
    path('blogs/', include('blogs.urls')),
    path('gallery/', include('gallery.urls')),
    path('events/', include('events.urls')),
    path('services/', include('services.urls')),
    path('reports/', include('reports.urls')),
    path('', include('pages.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)