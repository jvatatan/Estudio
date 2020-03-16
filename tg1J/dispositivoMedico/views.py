from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib import messages
from dispositivoMedico.models import DispositivoMedico
from dispositivoMedico.forms import DispositivoMedicoForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.core import serializers
import json
from datetime import date
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

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
        diasFaltantes = fechaVencimiento - hoy
        diasString =  str(diasFaltantes)
        startLoc = 0
        endLoc = 3
        diasString = diasString[startLoc: endLoc]
        print(diasFaltantes)
        print(int(diasString))
        print("color")
        if  int(diasString) > 0  and int(diasString) <= 90:
            print(self.object.asignacionColor)
            self.object.asignacionColor = 'Rojo'
            print(self.object.asignacionColor)
            self.object.save()
            print(self.object.asignacionColor)
            print("yo soy rojo")
        elif int(diasString) > 90 and int(diasString) <= 180:
            self.object.asignacionColor = 'Amarillo'
            self.object.save()
            print("soy amarillo")
        elif int(diasString) <= 0:
            self.object.asignacionColor = 'Naranja'
            self.object.save()
            print("soy naranja")
        else:
            self.object.asignacionColor = 'Verde' 
            self.object.save()
            print("soy verde")   
        return super().form_valid(form)
        
    def get_success_url(self):
        messages.success(self.request, 'El Dispositivo Medicó ' + self.object.nombre +' fue Registrado Exitosamente.')
        return super().get_success_url()    

class DispositivoMedicoList(LoginRequiredMixin, ListView):

    login_url = '/login/'
    redirect_field_name = '/login/'
    raise_exception = False
    model = DispositivoMedico
    queryset= model.objects.order_by('nombre') #queryset para ordenar mis datos al listar
    template_name = 'dispositivoMedico/listarDispositivosMedicos.html'

    def get_success_url(self):
        messages.success(self.request, 'El Dispositivo Medicó ' + self.object.nombre +' fue listado Exitosamente.')
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
        diasFaltantes = fechaVencimiento - hoy
        diasString =  str(diasFaltantes)
        startLoc = 0
        endLoc = 3
        diasString = diasString[startLoc: endLoc]
        print(diasFaltantes)
        print(int(diasString))
        print("color")
        if  int(diasString) > 0  and int(diasString) <= 90:
            print(self.object.asignacionColor)
            self.object.asignacionColor = 'Rojo'
            print(self.object.asignacionColor)
            self.object.save()
            print(self.object.asignacionColor)
            print("yo soy rojo")
        elif int(diasString) > 90 and int(diasString) <= 180:
            self.object.asignacionColor = 'Amarillo'
            self.object.save()
            print("soy amarillo")
        elif int(diasString) <= 0:
            self.object.asignacionColor = 'Naranja'
            self.object.save()
            print("soy naranja")
        else:
            self.object.asignacionColor = 'Verde' 
            self.object.save()
            print("soy verde")
        #actualizarColor(self.object.id)
        return super().form_valid(form)

    def get_success_url(self):
        messages.success(self.request, 'El Dispositivo Medicó ' + self.object.nombre +' fue modificado Exitosamente.')
        return super().get_success_url() 
        

class DispositivoMedicoDelete(LoginRequiredMixin, DeleteView):

    login_url = '/login/'
    redirect_field_name = '/login/'
    raise_exception = False
    model = DispositivoMedico
    form_class = DispositivoMedicoForm
    template_name = 'dispositivoMedico/eliminarDispositivoMedico.html'
    success_url = reverse_lazy('listarDispositivosMedicos')

    def get_success_url(self):
        messages.success(self.request, 'El Dispositivo Medicó ' + self.object.nombre +' fue eliminado Exitosamente.')
        return super().get_success_url() 

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
