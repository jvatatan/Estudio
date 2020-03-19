from django.conf.urls import url, include
from medicamentos.views import *

urlpatterns = [

    url(r'index', index, name='index'),
    #url(r'crearMedicamento', crearMedicamento, name='crearMedicamento'),
    #url(r'listarMedicamentos', listarMedicamentos, name='listarMedicamentos'),

   
    url(r'crearMedicamento', MedicamentoCreate.as_view(), name='crearMedicamento'),
    url(r'listarMedicamentos', MedicamentoList.as_view(), name='listarMedicamentos'),
    url(r'actualizarMedicamento/(?P<pk>\d+)/$', MedicamentoUpdate.as_view(), name='actualizarMedicamento'),
    url(r'eliminarMedicamento/(?P<pk>\d+)/$', MedicamentoDelete.as_view(), name='eliminarMedicamento'),
    url(r'^reporteMedicamentos/', reporteMedicamentos, name="reporteMedicamentos"),
    url(r'^buscarMedicamento/', buscarMedicamento, name="buscarMedicamento"),

]