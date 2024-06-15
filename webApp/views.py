from django.shortcuts import render,HttpResponse, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from .models import Flan, ContactForm
from . forms import ContacFormForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.
def inicio(request):
    #select * from flan;
    flanes = Flan.objects.all()
    
    #select * from WHERE is_private=False;
    flanes = Flan.objects.filter(id_private=False)
    
    contex = {
       "lista_flanes": flanes
    }
    return render (request, "index.html", contex)

def acerca(request):
    return render (request, "acerca.html",{})

@login_required
def bienvenido(request):
    #request.session['nombre']="Juan"
    flanes= Flan.objects.filter(id_private=True)
    contex = {
       "lista_flanes": flanes
    }
    return render (request, "bienvenido.html",contex)

def registro(request):
    if request.method =="POST":
        username = request.POST("username")
        email = request.POST("email")
        password = request.POST["password"]
        
        user = User.objects.create_user(username, email, password)  
        user.save()#inserta o actualiza
        
    return redirect ("/login")

def contacto(request):
    if request.method =="POST":
        form = ContacFormForm(request.POST)
        print(form)
        if form.is_valid():
            #aplicar logica
            form2 = ContactForm.objects.create(**form.cleaned_data)
            return redirect('/exito')
    else:
        form = ContacFormForm()   
        context ={
            "form": form
        }    
    return render (request, "contacto.html",context)

def exito(request):
    return render (request, "exito.html",{})

"""
def login(request):
    #get -> mostrar el html
    if request.metodo == "GET":
        return render (request,"login2.html")
    
    #post -> capturar datos desde el html
    if request.method =="POST":
        email = request.POST("email")
        password = request.POST["password"]
        #crear un objeto y asignar los valores
        #crear el registro en la base de datos
            #objeto.save()
            
        #uso de sesion
        
        request.session ["email"] = email
        
        return redirect("/")
"""    

