from django import forms
from django.forms import ModelForm
from django.core import validators

from .models import Reservas 

class ReservaForm(forms.Form):

    ESTADO = [('reserva','RESERVA'),('completada','COMPLETADA'),('anulada','ANULADA'),('no existe','NO EXISTE')]

    nombre = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    telefono = forms.CharField( widget=forms.TextInput(attrs={'class':'form-control'}))
    fecha = forms.DateTimeField( widget=forms.TextInput(attrs={'class':'form-control'}))
    hora = forms.TimeField ( widget=forms.TextInput(attrs={'class':'form-control'}))


    cantidad = forms.IntegerField(validators=[
        validators.MinValueValidator(1, 'cantidad minima de personas es 1'),
        validators.MaxValueValidator(15, 'cantidad maxima de personas es 15')
    ])


    estado = forms.CharField( widget=forms.Select(choices=ESTADO))
    estado.widget.attrs['class'] = 'form-control'


    observacion = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    observacion.required=False





    

class ReservaForm(ModelForm):
    class Meta:
        model = Reservas
        fields ='__all__'

    ESTADO = [('reserva','RESERVA'),('completada','COMPLETADA'),('anulada','ANULADA'),('no existe','NO EXISTE')]

    nombre = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    telefono = forms.CharField( widget=forms.TextInput(attrs={'class':'form-control'}))
    fecha = forms.DateTimeField(widget=forms.TextInput(attrs={'class':'form-control'}))
    hora = forms.TimeField (widget=forms.TextInput(attrs={'class':'form-control'}))


    cantidad = forms.IntegerField(validators=[
        validators.MinValueValidator(1, 'cantidad minima de personas es 1'),
        validators.MaxValueValidator(15, 'cantidad maxima de personas es 15')
    ])


    cantidad.widget.attrs['class']='form-control'

    estado = forms.CharField( widget=forms.Select(choices=ESTADO))
    estado.widget.attrs['class'] = 'form-control'


    observacion = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    observacion.required=False


