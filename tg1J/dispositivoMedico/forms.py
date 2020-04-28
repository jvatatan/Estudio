from django import forms
from dispositivoMedico.models import DispositivoMedico

class DispositivoMedicoForm(forms.ModelForm):

    class Meta:
        model = DispositivoMedico
        CHOICES = [('Escoge el color indicado','Escoge el color indicado'),('Rojo','Rojo'),('Amarillo', 'Amarillo'), ('Verde', 'Verde')]
        fields = [
                'nombre',
                'fecha_vencimiento',
                'fabricado_por',
                'registro_invima',
                'numero_lote',
                'presentacion_comercial',
                'forma_farmaceutica',
                'principio_activo',
                'unidad_medica',
                'porcentaje',
                'temperatura',
                'riesgo',
                'cantidad',
                'codigo',
                
        ]
        
        labels = {
                'nombre': 'Nombre',
                'fecha_vencimiento': 'Fecha Vencimiento',
                'fabricado_por': 'Fabricado por',
                'registro_invima': 'Registro Invima',
                'numero_lote': 'Número de Lote',
                'presentacion_comercial': 'Presentación Comercial',
                'forma_farmaceutica': 'Forma Farmacéutica',
                'principio_activo': 'Principio Activo',
                'unidad_medica': 'Unidad Médica',
                'porcentaje': 'Porcentaje',
                'temperatura': 'Temperatura',
                'riesgo': 'Riesgo',
                'cantidad': 'Cantidad',
                'codigo': 'Código',
                
        }

        widgets = {
                'Nombre':forms.TextInput(attrs={'class':'form-control form-control-dispositivoMedico'}),
                'fecha_vencimiento':forms.DateInput(attrs={'class':'form-control  form-control-user', 'type':'date','id':'myDate','value':'aaaa-mm-dd'}),
                'Fabricado_por':forms.TextInput(attrs={'class':'form-control form-control-dispositivoMedico'}),
                'Registro_invima':forms.TextInput(attrs={'class':'form-control form-control-dispositivoMedico'}),
                'Numero_lote':forms.TextInput(attrs={'class':'form-control form-control-dispositivoMedico'}),
                'Presentacion_comercial':forms.TextInput(attrs={'class':'form-control form-control-dispositivoMedico'}),
                'Forma_farmaceutica':forms.TextInput(attrs={'class':'form-control form-control-dispositivoMedico'}),
                'Principio_activo':forms.TextInput(attrs={'class':'form-control form-control-dispositivoMedico'}),
                'Unidad_medica':forms.TextInput(attrs={'class':'form-control form-control-dispositivoMedico'}),
                'Porcentaje':forms.TextInput(attrs={'class':'form-control form-control-dispositivoMedico'}),
                'Temperatura':forms.TextInput(attrs={'class':'form-control form-control-dispositivoMedico'}),
                'Riesgo':forms.TextInput(attrs={'class':'form-control form-control-dispositivoMedico'}),
                'Cantidad':forms.TextInput(attrs={'class':'form-control form-control-dispositivoMedico'}),
                'Codigo':forms.TextInput(attrs={'class':'form-control form-control-dispositivoMedico'}),
                
        }
