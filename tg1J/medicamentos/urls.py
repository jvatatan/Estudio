from django.conf.urls import url, include
from medicamentos.views import *

urlpatterns = [
    url(r'index', index, name='index'),
    url(r'crearMedicamento', MedicamentoCreate.as_view(), name='crearMedicamento'),
    url(r'listarMedicamentos', MedicamentoList.as_view(), name='listarMedicamentos'),
    url(r'ajax/decodeQRMedicamento', decodeQRMedicamento.as_view(), name='decodeQRMedicamento'),
    url(r'ajax/CreateQRForm', CreateQRForm.as_view(), name='createQRForm'),
    url(r'actualizarMedicamento/(?P<pk>\d+)/$', MedicamentoUpdate.as_view(), name='actualizarMedicamento'),
    url(r'ActualizarColorMedicamentos', ActualizarColorMedicamentos.as_view(), name='ActualizarColorMedicamentos'),
    url(r'eliminarMedicamento/(?P<pk>\d+)/$', MedicamentoDelete.as_view(), name='eliminarMedicamento'),
    url(r'^reporteMedicamentos/', reporteMedicamentos, name="reporteMedicamentos"),
    url(r'^buscarMedicamento/', buscarMedicamento, name="buscarMedicamento"),
    
    

]