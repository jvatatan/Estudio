from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from perfilUsuario.forms import UserForm
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Permission
from django.contrib import messages
from django.core.mail import EmailMessage
from medicamentos.models import Medicamento
from dispositivoMedico.models import DispositivoMedico
from django.core import serializers
import json
from datetime import date
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.models import AbstractUser

from django.conf import settings
from django.contrib.auth.hashers import check_password
from perfilUsuario.models import User


# Create your views here.
@login_required(login_url='/login/')
def indexWelocome(request):
    return render(request, 'paginaInicio/inicio.html')

""" 
@login_required(login_url='/login/')
def crearUsuario(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        form2 = RegistroUsuarioForm(request.POST)
        if form.is_valid() and form2.is_valid():
            form.save()
            form2.save()
            registro = RegistroUsuario.objects.all().last()
            registro.user_id = User.objects.all().last().id
            registro.save()
            messages.success(request, 'Usuario registrado con Exito')
        return HttpResponseRedirect(reverse('listarUsuarios')) #Se redirecciona a la pagina que desee
    else:
        form = UserForm()
        form2 = RegistroUsuarioForm()
        contexto = {'form':form,'form2':form2} 
    return render(request,'perfilUsuario/crearUsuario.html', contexto) 
   


@login_required(login_url='/login/')
def listarUsuarios(request):

    #perfilUsuario = User, RegistroUsuario.objects.all()
    perfilUsuario = User.objects.all()
    perfilUsuario = RegistroUsuario.objects.all()
    contexto = {'perfilUsuario':perfilUsuario}

    return render(request,'perfilUsuario/listarUsuarios.html',contexto)

@login_required(login_url='/login/')
def actualizarUsuario(request, id_user):
    perfilUsuario = User.objects.get(id=id_user)
    if request.method == 'GET':
        form = UserForm(instance=perfilUsuario)
        form2 = RegistroUsuarioForm(instance=perfilUsuario)
    else:
        form = UserForm(request.POST, instance=perfilUsuario)
        form2 = RegistroUsuarioForm(request.POST, instance=perfilUsuario)
        if form.is_valid() and form2.is_valid():
            form.save()
            form2.save()
            #contexto = {'perfilUsuario':perfilUsuario}
            contexto = {'form':form,'form2':form2} 

        return HttpResponseRedirect(reverse('listarUsuarios')) #Se redirecciona a la pagina que desee
    return render(request, 'perfilUsuario/crearUsuario.html', contexto)

@login_required(login_url='/login/')
def eliminarUsuario(request, id_user):
    perfilUsuario = User.objects.get(id_user)
    if request.method == 'POST':
        perfilUsuario.delete()
        #contexto = {'form':form,'form2':form2} 
        contexto = {'perfilUsuario':perfilUsuario} 

        return HttpResponseRedirect(reverse('listarUsuarios')) #Se redirecciona a la pagina que desee
    return render(request, 'perfilUsuario/eliminarUsuario.html', contexto)

 """


#esta clase es cuando me voy a registrar y no tengo cuenta en el login        
class CuentaCreateLogin(CreateView):
    
    model = User
    template_name = 'autentificacion/crearCuenta.html'
    form_class = UserForm
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super(CuentaCreateLogin, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] =self.form_class(self.request.GET)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        if form.is_valid(): 
            user = form.save(commit=False)
        
            user.save()
            messages.success(request, 'La creacion de cuenta para el Usuario '+ user.first_name + ' fue registrada exitosamente')
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))

 #____________________funciones basadas en clase para la construcion del CRUD______________________
 # NOTA: cuando tenemos una funcion vasada en clase tenemos que darle seguridad de la pagina se define de esta forma ejemplo
 #class UsuarioCreate(LoginRequiredMixin, CreateView):
    # login_url = '/login/
    # redirect_field_name = '/login/'
    # raise_exception = False
    # despues implementas lo de tu modelo o lo demas


class UsuarioCreate(LoginRequiredMixin, CreateView): 

    login_url = '/login/'
    redirect_field_name = '/login/'
    raise_exception = False
    model = User
    template_name = 'perfilUsuario/crearUsuario.html'
    form_class = UserForm
    success_url = reverse_lazy('listarUsuarios')

    def get_context_data(self, **kwargs):
        context = super(UsuarioCreate, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] =self.form_class(self.request.GET)
        return context

    def post(self, request, *args, **kwargs):
        
        self.object = self.get_object
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            messages.success(request, 'El Usuario ' + user.first_name + ' fue registrado exitosamente')
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))

class UsuarioList(LoginRequiredMixin,ListView):

    login_url = '/login/'
    redirect_field_name = '/login/'
    raise_exception = False
    model = User 
                                   
    template_name = 'perfilUsuario/listarUsuarios.html'

    def get_success_url(self):
        messages.success(self.request, 'El Usuario ' + self.object.first_name +'fue listado exitosamente.')
        return super().get_success_url()

    
class UsuarioUpdate(LoginRequiredMixin,UpdateView):

    login_url = '/login/'
    redirect_field_name = '/login/'
    raise_exception = False
    model = User
    template_name = 'perfilUsuario/actualizarUsuario.html'
    form_class = UserForm
    success_url = reverse_lazy('listarUsuarios')

    def get_context_data(self, **kwargs):
        context = super(UsuarioUpdate, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk',0)
        user =self.model.objects.get(id=pk)

        if 'form' not in context:
            context['form'] =self.form_class(instance=user)
        context['id'] = pk
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        id_user = kwargs['pk']
        user = self.model.objects.get(id=id_user)

        form = self.form_class(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'El usuario '+ user.first_name + ' fue modificado exitosamente') # esta linea es para llamar nuestro mensaje redactado
            return HttpResponseRedirect(self.get_success_url())
        else:
            return HttpResponseRedirect(self.get_success_url())
            #return self.render_to_response(self.get_context_data(form=form, form2=form2))


class UsuarioDelete(LoginRequiredMixin, DeleteView):
    
    login_url = '/login/'
    redirect_field_name = '/login/'
    raise_exception = False
    model = User
    template_name = 'perfilUsuario/eliminarUsuario.html'
    success_url = reverse_lazy('listarUsuarios')

    def get_success_url(self):
        messages.success(self.request, 'El Usuario ' + self.object.first_name + ' fue eliminado exitosamente.')
        return super().get_success_url()


# esta funcion es para vista de reportes graficos de usuarios.
@login_required(login_url='/login/') #esta linea de código es para la seguridad de la pagina cuando tenemos una función vasada en Funciones 
def reporteUsuarios(request):
    return render(request, 'reportes/reporteUsuarios.html')


#--------------------para el login------------------------

def userLogin(request):
	
        context = {}
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            print("hola estoy visitando")
            if user is not None:
                login(request, user)
                print("logue")
                if poderEnviarMensaje(construirString() , construirStringDispositivos()) == True:
                    print("1")
                    if request.GET.get('next', None):
                        return HttpResponseRedirect(request.GET['next'])
                    return HttpResponseRedirect(reverse('indexWelcome'))
                else:
                    print("2")
                    #enviarMensaje(request)  #linea de código para el envio del mensaje al usuario como notificación al email
                    if request.GET.get('next', None):
                        print("333")
                        return HttpResponseRedirect(request.GET['next'])
                    return HttpResponseRedirect(reverse('indexWelcome'))
            else:
                context["error"] = "El Nombre de Usuario o Contraseña incorreta verificar gracias!!"
                return render(request, "autentificacion/login.html", context)
        else:
            return render(request, "autentificacion/login.html", context)
            
@login_required(login_url='/login/')
def success(request):

    context = {}
    context['user'] = request.user
    return render(request, "autentificacion/login.html", context)
@login_required(login_url='/login/')
def userLogout(request):
    logout(request)
    return HttpResponseRedirect(reverse('indexLogin'))




# esta funcion es para renderizar al login.
@login_required(login_url='/login/') #esta linea de código es para la seguridad de la pagina cuando tenemos una función vasada en Funciones 
def indexLogin(request):
    return render(request, 'autentificacion/login.html')

# esta funcion es para renderizar al template de validacion de la nuevo  cambio de contraseña.
#@login_required(login_url='/login/') #esta linea de código es para la seguridad de la pagina cuando tenemos una función vasada en Funciones 
def nuevoCambioContraseña(request):
    return render(request, 'registrar/password_reset_complete.html')


#--------------------función para el envio de la notificacion al email de medicamento proximo a vencer------------------------
def construirString():

    medicamentos = str()
    medicamentosRojos = Medicamento.objects.filter(asignacionColor='Rojo')
    for object in medicamentosRojos: 
        medicamentos += object.nombre + " ,"
    return medicamentos

def construirStringDispositivos():

    dispositivos = str()
    dispositivosRojos = DispositivoMedico.objects.filter(asignacionColor='Rojo')
    for object in dispositivosRojos: 
        dispositivos += object.nombre + " ,"
    return dispositivos

def poderEnviarMensaje(construirStrings, construirStringDispositivos2):

    if not construirStringDispositivos2 and  not construirStrings:
        return True
    else: 
        return False

def enviarMensaje(request):
        correos = User.objects.all()
        correosFinal =list()
        message = ""
        if not construirString():
            message = "El o los  dispositivos medicos " + construirStringDispositivos() + " se encuentra en estado ROJO para vencer, por favor estar atentos."
        if not construirStringDispositivos():
            message = "El o los  medicamentos " + construirString() + " se encuentra en estado ROJO para vencer, por favor estar atentos."

        for object in correos:
                correosFinal = object.email
                email_message = EmailMessage(
                subject='Cambio de estado',
                body=message,
                from_email='clinicajva@gmail.com',
                to=[correosFinal],
        )
                email_message.send()
    
#---------estas funciones es para realizar una busqueda por filtro---------  
def buscar(request):
   
    identificacion = request.GET.get('identificacion') #esta linea es para un diccionario
    #select * from perfilUsuario where identificacion='identificacion'
    #select * from perfilUsuario where identificacion like '%identificacion'
    user = User.objects.filter(identificacion__startswith=identificacion) #lista de objectos user
    #users = User.objects.filter()
    user = [user_serializer(user) for user in user ] # lista de diccionario

    print(user)
    return HttpResponse(json.dumps(user), content_type='application/json')

def user_serializer(user):
    return {'id': user.id,'name': user.first_name,'tipo_usuario': user.tipo_usuario, 'tipo_identificacion': user.tipo_identificacion,
                'identificacion': user.identificacion,  'email': user.email, 'telefono': user.telefono, 'sexo': user.sexo}
                
    

#---------------------------para un formulario------------------------

#para un solo formulario create  vistas basadas en clase
'''class UsuarioCreate(CreateView):
    model = User
    form_class = UserForm
    form_class = RegistroUsuarioForm
    template_name = 'perfilUsuario/crearUsuario.html'
    success_url = reverse_lazy('listarUsuarios')'''

#listar 
'''class UsuarioList(ListView):
    model = RegistroUsuario                                    
    template_name = 'perfilUsuario/listarUsuarios.html'''

#autualizar para un solo formulario
'''class UsuarioUpdate(UpdateView):
    model = User
    model = RegistroUsuario
    form_class = UserForm
    form_class = RegistroUsuarioForm
    template_name = 'perfilUsuario/crearUsuario.html'
    success_url = reverse_lazy('listarUsuario')'''

#esto es para un formulario Delete
'''class UsuarioDelete(DeleteView):
    model = User
    model = RegistroUsuario
    form_class = UserForm
    form_class = RegistroUsuarioForm
    template_name = 'perfilUsuario/eliminarUsuario.html'
    success_url = reverse_lazy('listarUsuario')'''