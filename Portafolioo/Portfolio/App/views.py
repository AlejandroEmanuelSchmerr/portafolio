from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from .models import *
from .forms import *
from django.conf import settings
# Create your views here.


def inicio(request):
    return render(request,'index.html')

def acerca(request):
    return render(request,'acercade.html')

def contactos(request):
    #esta funcion utiliza el formukarioi
    if request.method == 'POST':
        miFormulario = FormContacto(request.POST)
        #LLEVAN VALIDACION IMPLICITA
        if miFormulario.is_valid():
            #Si el formulario es valido almaceno la informacion
            #a =miFormulario['mensaje'].value()
            #print(a)
            infoForm=miFormulario.cleaned_data

            #Envio correo a casilla del sitio
            send_mail(infoForm['asunto'],infoForm['mensaje'],infoForm.get('correo',''),['emanuelschmer777@gmail.com'],)
        
        #Envio correo respuesta automatica al usuario
            send_mail('Respuesta','Gracias ya nos estaremos comunicando',settings.EMAIL_HOST_USER,[infoForm.get('correo','')]) 
            
    else:
            #no se envio todavia crea un formulario vacio
            miFormulario=FormContacto()
    return render(request,"contacto.html",{"form":miFormulario})

def proyectos(request):
    proyectos = Proyecto.objects.all()
    return render(request, 'proyectos.html',{'proyectos': proyectos})



