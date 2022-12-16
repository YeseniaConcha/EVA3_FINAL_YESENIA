"""EVA3_FINAL_YESENIA URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from reservasAPP import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('reservas/',views.verReserva, name='reservas'),
    path('reservas/add/',views.addReserva, name='addReserva'),
    path('reservas/delete/<int:id>',views.deleteReserva, name='deleteReserva'),
    path('reservas/editar/<int:id>',views.editarReserva, name='editarReserva'),
    path('reservasApi/', views.reservaApi, name='reservaApi'),
    path('reservasApi/<int:pk>',views.detalleReserva, name='detalleReserva'),
]
