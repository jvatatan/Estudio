from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib import messages
from medicamentos.models import Medicamento
from medicamentos.forms import MedicamentoForm
from django.views.generic import View, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.core import serializers
import json
from datetime import date
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.serializers.json import DjangoJSONEncoder
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
    return render(request, 'medicamentos/index.html')

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
                    self.object.asignacionColor = 'Rojo'
                    self.object.save()
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
                    self.object.asignacionColor = 'Rojo'
                    self.object.save()
                elif int(diasString) > 90 and int(diasString) <= 180:
                    self.object.asignacionColor = 'Amarillo'
                    self.object.save()
                elif int(diasString) < 0:
                    self.object.asignacionColor = 'Naranja'
                    self.object.save()        
                else:
                    self.object.asignacionColor = 'Verde' 
                    self.object.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        messages.success(self.request, 'El Medicamento ' + self.object.nombre + ' fue Modificado Exitosamente.')
        return super().get_success_url()

# esta funcion es para generar la Actualizacion de todos los medicamentos.
class ActualizarColorMedicamentos(View):
    def get(self, request):
        hoy = date.today()
        medicamentos = Medicamento.objects.exclude(asignacionColor = 'Blanco')
        for medicamento in medicamentos:
            fecha = medicamento.fecha_vencimiento
            diferencia = fecha - hoy

            if int(diferencia.days) >= 0 and int(diferencia.days) <=90:
                medicamento.asignacionColor = 'Rojo'
                medicamento.save()
            elif int(diferencia.days) > 90 and int(diferencia.days) <=180:
                medicamento.asignacionColor = 'Amarillo'
                medicamento.save()
            elif int(diferencia.days) < 0:
                medicamento.asignacionColor = 'Naranja'
                medicamento.save()
            else:
                medicamento.asignacionColor = 'Verde'
                medicamento.save()

          
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

# esta funcion es para vista de reportes graficos de medicamentos.
@login_required(login_url='/login/') 
def reporteMedicamentos(request):
    medicamentoRojo = Medicamento.objects.filter(asignacionColor = 'Rojo').count()
    medicamentoAmarillo = Medicamento.objects.filter(asignacionColor = 'Amarillo').count()
    medicamentoVerde = Medicamento.objects.filter(asignacionColor = 'Verde').count()
    medicamentoBlanco = Medicamento.objects.filter(asignacionColor = 'Blanco').count()
    medicamentoNaranja = Medicamento.objects.filter(asignacionColor = 'Naranja').count()
    context = {'Rojo': medicamentoRojo, 'Amarillo': medicamentoAmarillo, 'Verde': medicamentoVerde, 'Blanco': medicamentoBlanco, 'Naranja': medicamentoNaranja}
    return render(request, 'reportes/reporteMedicamentos.html' , context)


# Esta es la funcion de la creacion de el codigo QR
class CreateQRForm(View):
    
    def  get(self, request):
        code = request.GET.get('code', None)
        nombre = request.GET.get('nombre', None)
        numero_lote =request.GET.get('numero_lote', None)
        qr = pyqrcode.create(code + numero_lote)
        nombreArchivo = nombre +".png"
        qr.png(nombreArchivo, scale=15)
        shutil.move(nombreArchivo, "C:/Users/JVA TATAN THE BEST/Desktop/GIT/proyectos/tg1J/static/img/imagenes/imagMedicamentoCódigoQR/" )
        qr.show()
        decodeQR(nombreArchivo)
        data = {
            'code': code,
            'nombre': nombre,
            'numero_lote': numero_lote
        }

def decodeQR(nombreArchivo):
    data = decode(Image.open(nombreArchivo))

class decodeQRMedicamento(View):
    def  get(self, request):
        nombreArchivo = request.GET.get('nombreArchivo', None)
        ruta = nombreArchivo[12:len(nombreArchivo)]
        rutaCompleta = "C:/Users/JVA TATAN THE BEST/Desktop/GIT/proyectos/tg1J/static/img/imagenes/imagMedicamentoCódigoQR/"+ ruta
        data = decode(Image.open(rutaCompleta))
        dataStr = str(data)
        palabra = dataStr.split("=")[1].split(",")[0]
        palabra = palabra [2:len(palabra)-1]
        data = {
            'code': palabra,

        }
        return JsonResponse(data)

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




""" import zbar
import numpy as np
import cv2
 
#Inicializar la camara
capture = cv2.VideoCapture(0)
 
#Cargar la fuente
font = cv2.FONT_HERSHEY_SIMPLEX
 
 
while 1:
    #Capturar un frame
    val, frame = capture.read()
 
    #Hay que comprobar que el frame sea valido
    if val:
        #Capturar un frame con la camara y guardar sus dimensiones
        frame_gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        dimensiones = frame_gris.shape #'dimensiones' sera un array que contendra el alto, el ancho y los canales de la imagen en este orden.
 
        #Convertir la imagen de OpenCV a una imagen que la libreria ZBAR pueda entender
        imagen_zbar = zbar.Image(dimensiones[1], dimensiones[0], 'Y800', frame_gris.tobytes())
 
        #Construir un objeto de tipo scaner, que permitira escanear la imagen en busca de codigos QR
        escaner = zbar.ImageScanner()
 
        #Escanear la imagen y guardar todos los codigos QR que se encuentren
        escaner.scan(imagen_zbar)
 
 
        for codigo_qr in imagen_zbar:
            loc = codigo_qr.location #Guardar las coordenadas de las esquinas
            dat = codigo_qr.data[:-2] #Guardar el mensaje del codigo QR. Los ultimos dos caracteres son saltos de linea que hay que eliminar
 
            #Convertir las coordenadas de las cuatro esquinas a un array de numpy
            #Asi, lo podremos pasar como parametro a la funcion cv2.polylines para dibujar el contorno del codigo QR
            localizacion = np.array(loc, np.int32)
 
            #Dibujar el contorno del codigo QR en azul sobre la imagen
            cv2.polylines(frame, [localizacion], True, (255,0,0), 2)
 
            #Dibujar las cuatro esquinas del codigo QR
            cv2.circle(frame, loc[0], 3, (0,0,255), -1) #Rojo - esquina superior izquierda
            cv2.circle(frame, loc[1], 3, (0,255,255), -1) #Amarillo - esquina inferior izquierda
            cv2.circle(frame, loc[2], 3, (255,100,255), -1) #Rosa -esquina inferior derecha
            cv2.circle(frame, loc[3], 3, (0,255,0), -1) #Verde - esquina superior derecha
 
 
            #Buscar el centro del rectangulo del codigo QR
            cx = (loc[0][0]+loc[2][0])/2
            cy = (loc[0][1]+loc[2][1])/2
 
            #Escribir el mensaje del codigo QR.
            cv2.putText(frame,dat,(cx,cy), font, 0.7,(255,255,255),2)
 
 
            #Calcular el angulo de rotacion del codigo QR. Supondremos que el angulo es la pendiente de la recta que une el vertice loc[0] (rojo) con loc[3] (verde)
            vector_director = [loc[3][0]-loc[0][0], loc[3][1]-loc[0][1]]
            angulo = (np.arctan2(float(vector_director[1]),vector_director[0])*57.29)%360 #Calculo de la tangente y conversion de radianes a grados
            #Correccion debida al orden de las coordenadas en la pantalla
            angulo += -360
            angulo *= -1
 
            #Escribir el angulo sobre la imagen con dos decimales
            cv2.putText(frame,str("%.2f" % angulo),(cx,cy+30), font, 0.7,(255,255,255),2)
 
        #Mostrar la imagen
        cv2.imshow('Imagen', frame)
 
    #Salir con 'ESC'
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
 
cv2.destroyAllWindows()
 """