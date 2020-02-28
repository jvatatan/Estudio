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
from django.urls import reverse_lazy
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^medicamentos/', include('medicamentos.urls')),
    url(r'^dispositivoMedico/', include('dispositivoMedico.urls')),
    url(r'^perfilUsuario/', include('perfilUsuario.urls')),
    url(r'^oauth/', include('social_django.urls', namespace='social')), 
    url(r'^login/', userLogin, name="userLogin"),
	url(r'^success/', success, name="userSuccess"),
	url(r'^logout/', userLogout, name="userLogout"),
    path('', TemplateView.as_view(template_name='login.html'), name='userLogin'),  
    #recuperacion de contraseña 
    url(
        r'^password/recovery/$',
        auth_views.PasswordResetView.as_view(
            template_name='registrar/password_reset_form.html',
            html_email_template_name='registrar/password_reset_email.html',
        ),
        name='password_reset',
    ),

    url(
        r'^password/recovery/done/$',
        auth_views.PasswordResetDoneView.as_view(
            template_name='registrar/password_reset_done.html',
        ),
        name='password_reset_done',
    ),
    url(
        r'^password/recovery/(?P<uidb64>[0-9A-Za-z_\-]+)/'
        r'(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(
            #success_url=reverse_lazy('home'),
            post_reset_login=True,
            template_name='registrar/password_reset_confirm.html',
            post_reset_login_backend=(
                'django.contrib.auth.backends.AllowAllUsersModelBackend'
            ),
        ),
        name='password_reset_confirm',
    ),

   


]

