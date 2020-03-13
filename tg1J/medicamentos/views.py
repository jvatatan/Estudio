from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from medicamentos.models import Medicamento
from medicamentos.forms import MedicamentoForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.core import serializers
import json
from datetime import date
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.serializers.json import DjangoJSONEncoder

# Create your views here.

def index(request):
    return render(request, 'medicamentos/index.html')

""" def crearMedicamento(request):
    if request.method == 'POST':
        form = MedicamentoForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('crearMedicamento')) #Se redirecciona a la pagina que desee
    else:
        form = MedicamentoForm()
        context = {'form':form} 
    return render(request,'medicamentos/crearMedicamento.html', context) 


def listarMedicamentos(request):

    medicamento = Medicamento.objects.all().order_by('id')
    context = {'medicamento':medicamento}
    return render(request,'medicamentos/listarMedicamentos.html',context) """

#______________________________________ actualizacion de asignacion de color________________________________________________

def actualizarColor(id):

    medicamento = Medicamento.objects.all().get(id=id)
    hoy = date.today()
    fechaVencimiento = medicamento.fecha_vencimiento
    diasFaltantes = fechaVencimiento - hoy
    diasString =  str(diasFaltantes)
    startLoc = 0
    endLoc = 3
    diasString = diasString[startLoc: endLoc]
    print(int(diasString))
    print("color")
    if  int(diasString) > 0  and int(diasString) <= 90:
        print(medicamento.asignacionColor)
        medicamento.asignacionColor = 'Rojo'
        print(medicamento.asignacionColor)
        medicamento.save()
        print(medicamento.asignacionColor)
        print("yo soy rojo")
    elif int(diasString) > 90 and int(diasString) <= 180:
        medicamento.asignacionColor = 'Amarillo'
        medicamento.save()
        print("soy amarillo")
    else:
        medicamento.asignacionColor = 'Verde' 
        medicamento.save()
        print("soy verde")
#____________________funciones basadas en clase para la construcion del CRUD______________________

class MedicamentoCreate(LoginRequiredMixin, CreateView):

    login_url = '/login/'
    redirect_field_name = '/login/'
    raise_exception = False
    model = Medicamento
    form_class = MedicamentoForm
    template_name = 'medicamentos/crearMedicamento.html'
    success_url = reverse_lazy('listarMedicamentos')


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
        else:
            self.object.asignacionColor = 'Verde' 
            self.object.save()
            print("soy verde")
        #actualizarColor(self.object.id)
        return super().form_valid(form)

    def get_success_url(self):
        messages.success(self.request, 'El Medicamento ' + self.object.nombre + ' fue Registrado Exitosamente.')
        return super().get_success_url()
    
        
class MedicamentoList(LoginRequiredMixin, ListView):

    login_url = '/login/'
    redirect_field_name = '/login/'
    raise_exception = False
    model = Medicamento
    queryset= model.objects.order_by('nombre')  #queryset para ordenar mis datos al listar
    template_name = 'medicamentos/listarMedicamentos.html'

    
    def get_success_url(self):
        messages.success(self.request, 'El Medicamento ' + self.object.nombre + ' fue listado Exitosamente.')
        return super().get_success_url()

class MedicamentoUpdate(LoginRequiredMixin, UpdateView):

    login_url = '/login/'
    redirect_field_name = '/login/'
    raise_exception = False
    model = Medicamento
    form_class = MedicamentoForm
    template_name = 'medicamentos/actualizarMedicamento.html'
    success_url = reverse_lazy('listarMedicamentos')

    def form_valid(self, form):
        self.object = form.save()       
        hoy = date.today()
        fechaVencimiento = self.object.fecha_vencimiento
        diasFaltantes = fechaVencimiento - hoy
        diasString =  str(diasFaltantes)
        startLoc = 0
        endLoc = 3
        diasString = diasString[startLoc: endLoc]
        if  int(diasString) > 0  and int(diasString) <= 90:
            self.object.asignacionColor = 'Rojo'   
            self.object.save()   
        elif int(diasString) > 90 and int(diasString) <= 180:
            self.object.asignacionColor = 'Amarillo'
            self.object.save()  
        else:
            self.object.asignacionColor = 'Verde' 
            self.object.save()
        #actualizarColor(self.object.id)
        return super().form_valid(form)
    
    def get_success_url(self):
        messages.success(self.request, 'El Medicamento ' + self.object.nombre + ' fue Modificado Exitosamente.')
        return super().get_success_url()

class MedicamentoDelete(LoginRequiredMixin, DeleteView):

    login_url = '/login/'
    redirect_field_name = '/login/'
    raise_exception = False
    model = Medicamento
    template_name = 'medicamentos/eliminarMedicamento.html'
    success_url = reverse_lazy('listarMedicamentos')

    
    def get_success_url(self):
        messages.success(self.request, 'El Medicamento ' + self.object.nombre + ' fue Eliminado Exitosamente.')
        return super().get_success_url()

#---------estas funciones es para realizar una busqueda por filtro---------  
def buscarMedicamento(request):
    if request.is_ajax:
        if request.method == 'GET':
            asignacionColor = request.GET.get('asignacionColor') #esta linea es para un diccionario
            medicamentos = Medicamento.objects.filter(asignacionColor__startswith = asignacionColor) #lista de objectos medicamentos
            medicamentos = [ medicamento_serializer(medicamento) for medicamento in medicamentos ] # lista de diccionario
            return HttpResponse(json.dumps(medicamentos,cls=DjangoJSONEncoder), content_type='application/json')
    
      
   
    

def medicamento_serializer(medicamento):
    return {'id': medicamento.id, 'nombre': medicamento.nombre, 'fabricado_por': medicamento.fabricado_por, 'registro_invima': medicamento.registro_invima,
                'numero_lote': medicamento.numero_lote, 'presentacion_comercial': medicamento.presentacion_comercial, 'forma_farmaceutica': medicamento.forma_farmaceutica, 'principio_activo': medicamento.principio_activo, 
                    'unidad_medica': medicamento.unidad_medica, 'porcentaje': medicamento.porcentaje, 'temperatura': medicamento.temperatura, 'cantidad': medicamento.cantidad, 'codigo': medicamento.codigo, 'asignacionColor': medicamento.asignacionColor}



