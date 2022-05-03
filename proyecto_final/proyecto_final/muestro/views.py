#En este archivo tengo que hacer el CRUD, la vista de las paginas, un formulario para mostrar los datos de la BD 
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from typing import Any, Dict
from django.shortcuts import render
from requests import request
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


from proyecto_final.muestro.models import Entrada, Usuario

class UserCreationsFormCustom(UserCreationForm):#re definimos esto por que sino no me deja guardar nuevos usuario en admin
    def save(self, commit: bool = True) :
        user = Usuario.objects.create(
            username=self.data['username'],
            password=self.data['password1']
        )
        return Usuario
    
class LoginView(TemplateView):#
    template_name= 'forms/login.html'
    def get(self, request):
        context={
            'form': AuthenticationForm()
        }
        return render(request, self.template_name, context)
    
    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form:
            user = request.POST.get('username')
            password = request.POST.get('password')
            
            user_auth = authenticate(username=user, password=password)
            if user_auth is not None:
                login(request, user_auth)
                return render(request,self.template_name, context={'message': f'Bienvenido{user}'})
            else:
                return render(request,self.template_name, context={'message': 'Datos ingresado incorrectos'})
        else:
            return render(request, self.template_name, context={'massage':'Datos incorrectos'})

class HomeView(TemplateView):

    Mostrar = 'forms/home.html'
    def get(self, request, status=None):#Envia informacion 
        context = {
            'entradas': Entrada.objects.all().order_by('-fecha')
        }
        return render(request, self.Mostrar, context)
    
class Registerview(TemplateView):#Esto es para crear un usuario en admin
    template_name = 'forms/registro.html'
    def get(self, request):
        context={
            'form': UserCreationForm()
        }
        return render(request, self.template_name, context)
    def post(self, request):
        form = UserCreationsFormCustom(request.POST)
        if form:
            form.save()
            return render(request,self.template_name, context={'message': 'Se creo el usuario correctamente'})
        else:
            return render(request,self.template_name, context={'message': 'ocurrio un error'})
 
class UsuarioCreate(CreateView):#Crea cursos ¿COMO HAGO PARA QUE EN EL CAMPO DE CONTRASEÑA NO SE VEA LA CONTRASEÑA?FUNCIONA
    model = Usuario#modelo del curso 
    template_name = 'forms/agregar.html'#direccion url para crear 
    success_url = "/"#donde nos redirecciona si se logra crear el curso PF NO ME MUESTRA EL MENSAJE PERO SI AGREGA LOS DATOS 
    fields = ['user', 'password', 'mail']#campos que interactuan al momento de creacion PF

class  EditarView(UpdateView):#Como hago para pasarle el ID pero no por un queryparants?FUNCIONA
    model = Usuario#modelo del curso 
    template_name = 'forms/editar.html'#direccion url para editar
    success_url = "/"#
    fields = ['user', 'password', 'mail']#campos que interactuan al momento de creacion PF

class  borrarview(DeleteView):#FUNCIONA
    model = Usuario#modelo del curso 
    template_name = 'forms/borrar.html'#direccion url para borrar
    success_url = "/"#donde nos redirecciona si se logra crear el curso PF NO ME MUESTRA EL MENSAJE PERO SI AGREGA LOS DATOS 
