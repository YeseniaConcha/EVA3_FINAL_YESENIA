from django.shortcuts import render, redirect

from reservasAPP.models import Reservas
from reservasAPP.forms import *
from django.http import JsonResponse
from rest_framework.response import Response 
from rest_framework import status
from rest_framework.decorators import api_view
from reservasAPP.serializers import *
# Create your views here.
def index(request):
    return render(request, 'index.html')

def verReserva(request):
    reservas = Reservas.objects.all()
    return render(request, 'verreservas.html', {'reservas':reservas})


def addReserva(request):
    data={
        'titulo': 'Crear Reserva',
        'form': ReservaForm()
    }
    if (request.method) == 'POST':
        formulario = ReservaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('/reservas')
        else:
            data['form'] = formulario
    return render(request, 'reservaform.html', data)

def deleteReserva(request, id):
    reserva = Reservas.objects.get(id=id)
    reserva.delete()
    return redirect("/reservas")

def editarReserva(request, id):
    reserva = Reservas.objects.get(id=id)
    data = {
        'form':ReservaForm(instance=reserva), 
        'titulo':'Editar reserva'
        }
    if (request.method == 'POST'):
        form = ReservaForm(request.POST, instance=reserva)
        if (form.is_valid()):
            form.save()
            return redirect('/reservas')
        else:
            data['form'] = form
    return render(request, 'reservaform.html', data)


@api_view(['GET', 'POST'])
def reservaApi(request):
    if (request.method == 'GET'):
        reser = Reservas.objects.all()
        serializer = reservaSerializer(reser, many=True)
        return Response (serializer.data)


    if request.method == 'POST':
        serializer = reservaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def detalleReserva(request, pk):
    try:
        reser = Reservas.objects.get(pk=pk)
    except Reservas.DoesNotExist:
        return Response(starus=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = reservaSerializer(reser)
        return Response(serializer.data)


    #actualizar datos de una reserva
    if request.method == "PUT":
        serializer = reservaSerializer(reser, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #eliminar datos de una reserva
    if request.method == "DELETE":
        reser.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    



