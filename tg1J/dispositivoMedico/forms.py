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
                'Nombre': 'nombre',
                'Fecha Vencimiento': 'fecha_vencimiento',
                'Fabricado Por': 'fabricado_por',
                'Registro Invima': 'registro_invima',
                'Numero Lote': 'numero_lote',
                'Presentacion Comercial': 'presentacion_comercial',
                'Forma Farmaceutica': 'forma_farmaceutica',
                'Principio Activo': 'principio_activo',
                'Unidad Medica': 'unidad_medica',
                'Porcentaje': '%',
                'Temperatura': 'C°',
                'Riesgo': 'riesgo',
                'Cantidad': '0000...',
                'Codigo': '0000..',
                
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
