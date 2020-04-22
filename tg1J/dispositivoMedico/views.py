from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib import messages
from dispositivoMedico.models import DispositivoMedico
from dispositivoMedico.forms import DispositivoMedicoForm
from django.views.generic import View, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.core import serializers
import json
from datetime import date
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
# esto es lo del codigo QR
import pyqrcode
import png
from PIL import Image, ImageOps
from pyzbar.pyzbar import decode
# esto es para la ruta de almacenamiento de la imagen cuando generamos el c'odigo QR
import shutil

# Create your views here.
@login_required(login_url='/login/') 
def index(request):
    return render(request, 'dispositivoMedico/index.html')

""" def crearDispositivoMedico(request):
    if request.method == 'POST':
        form = DispositivoMedicoForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('crearDispositivoMedico')) #Se redirecciona a la pagina que desee
    else:
        form = DispositivoMedicoForm()
        context = {'form':form} 
    return render(request,'dispositivoMedico/crearDispositivoMedico.html', context) 


def listarDispositivosMedeicos(request):

    dispositivoMedico = DispositivoMedico.objects.all()
    context = {'dispositivoMedico':dispositivoMedico}
    return render(request,'dispositivoMedico/listarDispositivosMedicos.html',context) """

#______________________________________ actualización de asignación de color________________________________________________

def actualizarColor(id):

    dispositivoMedico = DispositivoMedico.objects.all().get(id=id)
    hoy = date.today()
    fechaVencimiento = dispositivoMedico.fecha_vencimiento
    diasFaltantes = fechaVencimiento - hoy
    diasString =  str(diasFaltantes)
    startLoc = 0
    endLoc = 3
    diasString = diasString[startLoc: endLoc]

    if  int(diasString) > 0  and int(diasString) <= 90:
        dispositivoMedico.asignacionColor = 'Rojo'
        dispositivoMedico.save()
    elif int(diasString) > 90 and int(diasString) <= 180:
        dispositivoMedico.asignacionColor = 'Amarillo'
        dispositivoMedico.save()
    elif int(diasString) <= 0:
        dispositivoMedico.asignacionColor = 'Naranja'
        dispositivoMedico.save()    
    else:
        dispositivoMedico.asignacionColor = 'Verde' 
        dispositivoMedico.save()
#______________________________________ registro basados en clase_________________________________________________

class DispositivoMedicoCreate(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = '/login/'
    raise_exception = False
    model = DispositivoMedico
    form_class = DispositivoMedicoForm
    template_name = 'dispositivoMedico/crearDispositivoMedico.html'
    success_url = reverse_lazy('listarDispositivosMedicos')

    def form_valid(self, form):
        self.object = form.save()       
        hoy = date.today()
        fechaVencimiento = self.object.fecha_vencimiento
        if fechaVencimiento == None:
            self.object.asignacionColor = 'Blanco'
        else:    
            diasFaltantes = fechaVencimiento - hoy
            diasString =  str(diasFaltantes)
            startLoc = 0
            endLoc = 3
            diasString = diasString[startLoc: endLoc]
            if diasString.isdigit() == False:
                self.object.asignacionColor = 'Rojo'
                self.object.save()
            else:

                if  int(diasString) >= 0  and int(diasString) <= 90:
                    print(self.object.asignacionColor)
                    self.object.asignacionColor = 'Rojo'
                    print(self.object.asignacionColor)
                    self.object.save()
                    print(self.object.asignacionColor)
                elif int(diasString) > 90 and int(diasString) <= 180:
                    self.object.asignacionColor = 'Amarillo'
                    self.object.save()
                elif int(diasString) < 0:
                    self.object.asignacionColor = 'Naranja'
                    self.object.save()        
                else:
                    self.object.asignacionColor = 'Verde' 
                    self.object.save()
            #actualizarColor(self.object.id)
        return super().form_valid(form)

    
    def get_success_url(self):
        messages.success(self.request, 'El Dispositivo Médico ' + self.object.nombre +' fue Registrado Exitosamente.')
        return super().get_success_url()    

class DispositivoMedicoList(LoginRequiredMixin, ListView):

    login_url = '/login/'
    redirect_field_name = '/login/'
    raise_exception = False
    model = DispositivoMedico
    queryset= model.objects.order_by('nombre') #queryset para ordenar mis datos al listar
    template_name = 'dispositivoMedico/listarDispositivosMedicos.html'

    def get_success_url(self):
        messages.success(self.request, 'El Dispositivo Médico ' + self.object.nombre +' fue listado Exitosamente.')
        return super().get_success_url() 

class DispositivoMedicoUpdate(LoginRequiredMixin, UpdateView):

    login_url = '/login/'
    redirect_field_name = '/login/'
    raise_exception = False
    model = DispositivoMedico
    form_class = DispositivoMedicoForm
    template_name = 'dispositivoMedico/actualizarDispositivoMedico.html'
    success_url = reverse_lazy('listarDispositivosMedicos')

    def form_valid(self, form):
        self.object = form.save()       
        hoy = date.today()
        fechaVencimiento = self.object.fecha_vencimiento
        if fechaVencimiento == None:
            self.object.asignacionColor = 'Blanco'

        else:
            diasFaltantes = fechaVencimiento - hoy
            diasString =  str(diasFaltantes)
            print(diasFaltantes)
            startLoc = 0
            endLoc = 3
            print(startLoc)
            print(endLoc)
            diasString = diasString[startLoc: endLoc ]
            print(diasFaltantes)
            if diasString.isdigit() == False:
                self.object.asignacionColor = 'Rojo'
                self.object.save()
                print("yo soy color rojo")
            else:

                if  int(diasString) >= 0  and int(diasString) <= 90:
                    print(self.object.asignacionColor)
                    self.object.asignacionColor = 'Rojo'
                    print(self.object.asignacionColor)
                    self.object.save()
                    print(self.object.asignacionColor)
                elif int(diasString) > 90 and int(diasString) <= 180:
                    self.object.asignacionColor = 'Amarillo'
                    self.object.save()
                elif int(diasString) < 0:
                    self.object.asignacionColor = 'Naranja'
                    self.object.save()        
                else:
                    self.object.asignacionColor = 'Verde' 
                    self.object.save()
            #actualizarColor(self.object.id)
        return super().form_valid(form)

    def get_success_url(self):
        messages.success(self.request, 'El Dispositivo Médico ' + self.object.nombre +' fue modificado Exitosamente.')
        return super().get_success_url() 

# esta funcion es para generar la Actualizacion de todos los dispositivo.
class ActualizarColorDispositivos(View):
    def get(self, request):
        hoy = date.today()
        dispositivos = DispositivoMedico.objects.exclude(asignacionColor = 'Blanco')
        for dispositivo in dispositivos:
            fecha = dispositivo.fecha_vencimiento
            diferencia = fecha - hoy
            print('soy el dispositivo  ' + str(dispositivo.id) + 'con color anterior' + dispositivo.asignacionColor)
            if int(diferencia.days) >= 0 and int(diferencia.days) <=90:
                dispositivo.asignacionColor = 'Rojo'
                dispositivo.save()
                print('soy el dispositivo' + str(dispositivo.id) + 'con color actual' + dispositivo.asignacionColor)
            elif int(diferencia.days) > 90 and int(diferencia.days) <=180:
                dispositivo.asignacionColor = 'Amarillo'
                dispositivo.save()
                print('soy el dispositivo' + str(dispositivo.id) + 'con color actual' + dispositivo.asignacionColor)
            elif int(diferencia.days) < 0:
                dispositivo.asignacionColor = 'Naranja'
                dispositivo.save()
                print('soy el dispositivo' + str(dispositivo.id) + 'con color actual' + dispositivo.asignacionColor)
            else:
                dispositivo.asignacionColor = 'Verde'
                dispositivo.save()
                print('soy el dispositivo' + str(dispositivo.id) + 'con color actual' + dispositivo.asignacionColor)


class DispositivoMedicoDelete(LoginRequiredMixin, DeleteView):

    login_url = '/login/'
    redirect_field_name = '/login/'
    raise_exception = False
    model = DispositivoMedico
    form_class = DispositivoMedicoForm
    template_name = 'dispositivoMedico/eliminarDispositivoMedico.html'
    success_url = reverse_lazy('listarDispositivosMedicos')

    def get_success_url(self):
        messages.success(self.request, 'El Dispositivo Médico ' + self.object.nombre +' fue eliminado Exitosamente.')
        return super().get_success_url() 


# esta funcion es para vista de reportes graficos de dispositivos medicos.
@login_required(login_url='/login/') 
def reporteDispositivosMedicos(request):
    dispositivoMedicosRojo = DispositivoMedico.objects.filter(asignacionColor ='Rojo').count()
    dispositivoMedicosAmarrillo = DispositivoMedico.objects.filter(asignacionColor ='Amarillo').count()
    dispositivoMedicosVerde = DispositivoMedico.objects.filter(asignacionColor ='Verde').count()
    dispositivoMedicosBlanco = DispositivoMedico.objects.filter(asignacionColor ='Blanco').count()
    dispositivoMedicosNaranja = DispositivoMedico.objects.filter(asignacionColor ='Naranja').count()
    context = {'Rojo': dispositivoMedicosRojo, 'Amarillo': dispositivoMedicosAmarrillo, 'Verde': dispositivoMedicosVerde, 'Blanco': dispositivoMedicosBlanco, 'Naranja': dispositivoMedicosNaranja}
    return render(request, 'reportes/reporteDispositivosMedicos.html' , context)

# Esta es la funcion de la creacion de el codigo QR
class CreateQRForm_dispositivo(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = '/login/'
    raise_exception = False
    
    def  get(self, request):
        code = request.GET.get('code', None)
        nombre = request.GET.get('nombre', None)
        print(nombre)
        qr = pyqrcode.create(code)
        nombreArchivo = nombre +".png"
        qr.png(nombreArchivo, scale=15)
        qr.show()
        shutil.move(nombreArchivo, "C:/Users/JVA TATAN THE BEST/Desktop/GIT/proyectos/tg1J/static/img/imagenes/imagDispositivoMédicoCódigoQR")
        decodeQR(nombreArchivo)
        data = {
            'code': code,
            'nombre': nombre
        }

def decodeQR(nombreArchivo):
    data = decode(Image.open(nombreArchivo))
    print(data)


#---------estas funciones es para realizar una busqueda por filtro---------  
def buscarDispositivoMedico(request):
   
    asignacionColor = request.GET.get('asignacionColor') #esta linea es para un diccionario
    #select * from medicamentos where asgnacionColor='asignacionColor'
    #select * from medicamentos where asgnacionColor like '%asignacionColor'
    dispositivoMedicos = DispositivoMedico.objects.filter(asignacionColor__startswith=asignacionColor) #lista de objectos medicamentos
    dispositivoMedicos = [ dispositivoMedico_serializer(dispositivoMedico) for dispositivoMedico in dispositivoMedicos ] # lista de diccionario
    print(dispositivoMedicos)
    return HttpResponse(json.dumps(dispositivoMedicos), content_type='application/json')

def dispositivoMedico_serializer(dispositivoMedico):
    return {'id': dispositivoMedico.id, 'nombre': dispositivoMedico.nombre, 'fabricado_por': dispositivoMedico.fabricado_por, 'registro_invima': dispositivoMedico.registro_invima,
                'numero_lote': dispositivoMedico.numero_lote, 'presentacion_comercial': dispositivoMedico.presentacion_comercial, 'forma_farmaceutica': dispositivoMedico.forma_farmaceutica, 'principio_activo': dispositivoMedico.principio_activo, 
                    'unidad_medica': dispositivoMedico.unidad_medica, 'porcentaje': dispositivoMedico.porcentaje, 'temperatura': dispositivoMedico.temperatura, 'riesgo': dispositivoMedico.riesgo, 'cantidad': dispositivoMedico.cantidad, 'codigo': dispositivoMedico.codigo, 'asignacionColor': dispositivoMedico.asignacionColor}
