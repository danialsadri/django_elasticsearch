from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls', namespace='home')),
]
admin.sites.AdminSite.index_title = 'مدیریت وبسایت'
admin.sites.AdminSite.site_title = 'مدیریت وبسایت'
admin.sites.AdminSite.site_header = 'مدیریت وبسایت'
