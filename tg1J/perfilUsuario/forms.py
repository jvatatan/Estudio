from django import forms
from django.contrib.auth.forms  import UserCreationForm

from perfilUsuario.models import User

class UserForm(UserCreationForm):

	class Meta:
		model = User
		CHOICES = [('Cédula de Ciudadanía', 'Cédula de Ciudadanía'), ('Cédula Extranjera', 'Cédula Extrangera'), ('Pasaporte', 'Pasaporte')]
		CHOICES2 = [('Femenino', 'Femenino'), ('Masculino', 'Masculino'), ('Otro', 'Otro')]

		
		fields = [
				'username',
				'first_name',
				'last_name',
				'email',
				'password1',
				'password2',
				'tipo_identificacion',
                'identificacion',
                'telefono',
				'sexo',
		]
		labels = {
				'username': 'Nombre de Usuario',
				'first_name': 'Nombre',
				'last_name': 'Apellidos',
				'email': 'Correo Electrónico',
				'password1': 'Contraseña',
				'password2': 'Confirmación de Contraseña',
				'tipo_identificacion': 'Tipo Identificacion',
                'identificacion': 'Número de Identificacion',
                'telefono': 'Telefono',
				'sexo': 'Sexo',
		}
		widgets = {
				'username':forms.TextInput(attrs={'class':'form-control form-control-user'}),
				'first_name':forms.TextInput(attrs={'class':'form-control form-control-user'}),
				'last_name':forms.TextInput(attrs={'class':'form-control form-control-user'}),
				'email':forms.TextInput(attrs={'class':'form-control form-control-user'}),
				'password1':forms.CharField(widget=forms.PasswordInput()),
				'password2':forms.CharField(widget=forms.PasswordInput()),
				'tipo_identificacion':forms.Select(choices=CHOICES),
                'identificacion':forms.TextInput(attrs={'class':'form-control form-control-user'}),
                'telefono':forms.TextInput(attrs={'class':'form-control form-control-user'}),
				'sexo':forms.Select(choices=CHOICES2),
		}
