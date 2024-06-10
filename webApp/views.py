from django.shortcuts import render,HttpResponse, redirect
from .models import Flan, ContactForm
from . forms import ContacFormForm

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

def bienvenido(request):
    flanes= Flan.objects.filter(id_private=True)
    contex = {
       "lista_flanes": flanes
    }
    return render (request, "bienvenido.html",contex)

def registro(request):
    return render(request,"registro.html",{})

def contacto(request):
    if request.method =="POST":
        form = ContacFormForm(request.POST)
        if form.is_valid():
            #aplicar logica
            form2 = ContactForm.objects.create(**form.cleaned_data)
            return redirect('/')
    else:
        form = ContacFormForm()   
        context ={
            "form": form
        }    
    return render (request, "contacto.html",context)


"""def login(request):
    #get -> mostrar el html
    if request.metodo == "GET":
        return render (request,"login.html")
    
    #post -> capturar datos desde el html
    if request.method =="POST":
        print(request.POST)
        print(request.POST)["email"]
        print(request.POST)["password"]
        email = request.POST
        password = Request.POST["password"]
        #crear un objeto y asignar los valores
        #crear el registro en la base de datos
            #objeto.save()
            
        #uso de sesion
        
        request.session ["email"] = email
        
        return redirect("/")
""" 
"""        
def contacto(request):
    if request.method == 'POST':
        form = ContactFormForm(request.POST)
        print(form)
        if form.is_valid():
            #aplicar logica
            form2 = ContactForm.objects.create(**form.cleaned_data)
            return redirect('/')
    else:
        form = ContactFormForm()
        context ={
            "form": form
        }
    return render(request,"contacto.html",context)
"""