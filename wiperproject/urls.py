from django.contrib import admin
# from django.contrib.auth import views as auth_views

from django.conf.urls import handler404
from wiper.views import custom_404_view

from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.views.static import serve

from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('wiper.urls')),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = custom_404_view
