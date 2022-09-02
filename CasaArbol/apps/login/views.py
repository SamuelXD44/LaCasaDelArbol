from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import CustomUserCreationForm
from django.contrib import messages
# Create your views here.

def registro(request):
   usuario= {
        'formulario': CustomUserCreationForm ()
    }
   if request.method =='POST':
        formulario= CustomUserCreationForm(data= request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"],password=formulario.cleaned_data["password1"])
            login(request,user)
            messages.success(request,"Registro Exitoso")
            #redirijo al index
            return redirect(to="index")
        usuario["formulario"]=formulario    
            
   return render(request,'registration/registro.html', usuario )
   
