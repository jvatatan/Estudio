#from django.urls import path
from django.conf.urls import url, include
from perfilUsuario.views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'index', indexWelocome, name='indexWelcome'),
    url(r'crearUsuario', UsuarioCreate.as_view(), name='crearUsuario'),
    url(r'crearCuenta', CuentaCreateLogin.as_view(), name='crearCuenta'),
    url(r'listarUsuarios', UsuarioList.as_view(), name='listarUsuarios'),
    url(r'actualizarUsuario/(?P<pk>\d+)/$', UsuarioUpdate.as_view(), name='actualizarUsuario'),
    url(r'eliminarUsuario/(?P<pk>\d+)/$', UsuarioDelete.as_view(), name='eliminarUsuario'),
    url(r'^indexLogin/', indexLogin, name="indexLogin"),
    url(r'^reporteUsuarios/', reporteUsuarios, name="reporteUsuarios"),
    url(r'^buscar/', buscar, name="buscar"),


]