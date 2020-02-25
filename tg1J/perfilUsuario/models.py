from django.db import models

from django.utils.translation import ugettext as _
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField
from django.contrib.auth.models import AbstractUser
from perfilUsuario.managers import CustomManager

# Create your models here.
#user = models.ForeignKey(User, null=False, blank=True, on_delete=models.CASCADE)
class User(AbstractUser):
   
   tipo_usuario = models.CharField(max_length=20, default='Empleado')
   tipo_identificacion = models.CharField(max_length=20)
   identificacion = models.BigIntegerField()
   telefono = models.BigIntegerField()
   sexo = models.CharField(max_length=20)

   objects = CustomManager()

   REQUIRED_FIELDS=["tipo_identificacion", "identificacion", "telefono", "sexo", "email"]

        

   def guardarDatos(self, tipo_usuario, tipo_identificacion, identificacion, telefono, sexo, user):
      nuevoUser = User(
         tipo_usuario=tipo_usuario, tipo_identificacion=tipo_identificacion,
          identificacion=identificacion, telefono=telefono, sexo=sexo, user=user)
      nuevoUser.save()

   class Meta:

         permissions = {
            ('Empleado', _('Empleado')),
         }     
        
        
        
        #def __str__(self):
           # return self.identificacion
        
        #def __str__(self):
           # return '{}'.format(self.identificacion)
