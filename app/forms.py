from email.policy import default
from multiprocessing.sharedctypes import Value
from tkinter import Widget
from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User
from .validators import MaxSizeFileValidator
#FORMULARIO
#class FormularioUserRegistro(UserCreationForm):
#   class Meta:
#        model = Cliente
#        fields = 'nom_cli','ap_cli','run_cli','fono','comuna','direccion','correo','password','foto','suscripcion'
#LOS NOMBRE DE LAS COLUMNAS QUE SE VISUALIZAN EN LA PAGINA ESTAN EN LA BASE DE DATOS SQLITE 


class ProductoForm(forms.ModelForm):
    nombre = forms.CharField(min_length=10,max_length=40)
    desc = forms.CharField(min_length=3,max_length=150)
    precio = forms.IntegerField(min_value=500, max_value=1000000)
    img = forms.ImageField(required=False, validators=[MaxSizeFileValidator(max_size_file=2)])
        
    class Meta:
        model = Producto
        fields = 'codigo','nombre','desc','precio','stock','tipo','img'
        
        widgets = {
            'fecha_ingreso' : forms.SelectDateWidget(years=range(2020,2023))
        }

class DatosPersonalesForm(ModelForm):
    nom_cli = forms.CharField(min_length=3, max_length=150)
    foto = forms.ImageField(required=False, validators=[MaxSizeFileValidator(max_size_file=2)])
    ap_cli = forms.CharField(min_length=3, max_length=150)
    run_cli = forms.CharField(min_length=8, max_length=9)
    class Meta:
        model = Cliente
        fields =[ 'nom_cli', 'ap_cli', 'run_cli', 'fono', 'comuna', 'direccion', 'correo', 'foto']

class RegistroForm(UserCreationForm):
    pass

        