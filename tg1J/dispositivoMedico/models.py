from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField
# Create your models here.
class DispositivoMedico(models.Model):

   nombre = models.CharField(max_length = 40)
   fecha_vencimiento = models.DateField(blank=True, null=True)
   fabricado_por = models.CharField(max_length = 40)
   registro_invima = models.CharField(max_length = 40)
   numero_lote = models.CharField(max_length = 40)
   presentacion_comercial = models.CharField(max_length = 40, blank=True)
   forma_farmaceutica = models.CharField(max_length = 40, blank=True)
   principio_activo = models.CharField(max_length = 40, blank=True)
   unidad_medica = models.CharField(max_length = 40)
   porcentaje = models.CharField(max_length = 40, blank=True)
   temperatura = models.CharField(max_length = 40, blank=True)
   riesgo = models.CharField(max_length = 40)
   cantidad = models.IntegerField()
   codigo = models.CharField(max_length = 60, blank=True)
   asignacionColor = models.CharField(max_length = 30, default="Blanco")


    
   def guardarDatosDispositivoMedico(self, nombre, fecha_vencimiento, fabricado_por, registro_invima, numero_lote, presentacion_comercial,
                                 forma_farmaceutica, principio_activo, unidad_medica, porcentaje, temperatura, riesgo, cantidad, codigo, asignacionColor):
      nuevoRegistroDispositivoMedico = DispositivoMedico(
         nombre=nombre, fecha_vencimiento=fecha_vencimiento, fabricado_por=fabricado_por, registro_invima=registro_invima, numero_lote=numero_lote, presentacion_comercial=presentacion_comercial,
                                 forma_farmaceutica=forma_farmaceutica, principio_activo=principio_activo, unidad_medica=unidad_medica, porcentaje=porcentaje, temperatura=temperatura, riesgo=riesgo, cantidad=cantidad, codigo=codigo, asignacionColor=asignacionColor)
      nuevoRegistroDispositivoMedico.save()

        
        
        
        
      #def __str__(self):
         # return self.identificacion
        
      #def __str__(self):
         # return '{}'.format(self.identificacion)