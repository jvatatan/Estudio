from django.contrib import admin
#from perfilUsuario.models import RegistroUsuario
from perfilUsuario.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .models import User

# Register your models here.
#admin.site.register(User)
#admin.site.register(RegistroUsuario)

#class CustomUserAdmin(UserAdmin):
#    add_form = UserForm
#    form = RegistroUsuarioForm
#    model = User
#    list_display = ['email', 'username',]

#admin.site.register(User, CustomUserAdmin)