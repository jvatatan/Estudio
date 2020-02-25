"""tg1J URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from perfilUsuario.views import userLogin, userLogout, success
from django.conf import settings
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^medicamentos/', include('medicamentos.urls')),
    url(r'^dispositivoMedico/', include('dispositivoMedico.urls')),
    url(r'^perfilUsuario/', include('perfilUsuario.urls')),
    url(r'^oauth/', include('social_django.urls', namespace='social')), 
    url(r'^login/', userLogin, name="userLogin"),
	url(r'^success/', success, name="userSuccess"),
	url(r'^logout/', userLogout, name="userLogout"),
    path('', TemplateView.as_view(template_name='login.html'), name='login'),
    #url(r'^$', login, {'templates_name':'login.html'}, name='login'),
    #url(r'^reset/password_reset', password_reset, {'template_name':'registrar/password_reset_form.html', 'email_template':'registrar/password_reset_email.html'}, name='password_reset'),
    #url(r'^reset/password_reset_done', password_reset_done, {'template_name':'registrar/password_reset_done.html'}, name='password_reset_done'),
    #url(r'^reset/(?P<uidb64>[0-9A-Za-z\-].+)/(?P<token>.+)/$', password_reset_confirm, {'template_name':'registrar/password_reset_confirm.html'}, name='password_reset_confirm'),
    #url(r'^reset/done', password_reset_complete, {'template_name':'registrar/password_reset_complete.html'}, name='password_reset_complete'),    
    url('^', include('django.contrib.auth.urls')),





]
