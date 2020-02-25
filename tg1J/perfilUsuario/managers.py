from django.contrib.auth.models import UserManager

class CustomManager(UserManager):

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('tipo_usuario', "Administrador")
        if extra_fields.get('tipo_usuario') != "Administrador":
            raise ValueError('Superuser must have tipo_usuario="Administrador".')
        
        return super().create_superuser(username, password=None, **extra_fields)