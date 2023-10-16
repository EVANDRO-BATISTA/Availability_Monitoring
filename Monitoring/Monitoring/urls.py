from django.contrib import admin
from django.urls import path, include
from monit_availability import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login, name='dashboard'),
    path('login', views.login, name='login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('config', views.config, name='config'),
    path('add_ips', views.add_ips, name='add_ips'),
    path('relatorio', views.relatorio, name='relatorio'),
    path('accounts/', include('django.contrib.auth.urls')),    
]
