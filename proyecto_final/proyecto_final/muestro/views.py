#En este archivo tengo que hacer el CRUD, la vista de las paginas, un formulario para mostrar los datos de la BD 
from pyexpat import model
from re import template
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from typing import Any, Dict
from django.shortcuts import render
from requests import request
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


from proyecto_final.muestro.models import Entrada, Mensaje
from proyecto_final.users.models import User

#corregir para que aparezca mi login 
#hacer el crud de entrada(titulo,mensaje,fecha,subtitulo)
#crear los archivos htmls   

class UserCreationsFormCustom(UserCreationForm):#re definimos esto por que sino no me deja guardar nuevos usuario en admin
    def save(self, commit: bool = True) -> User :
        user = User.objects.create(
            username=self.data['username']
        )
        User.set_password(user, raw_password=self.data['password1'])
        user.save()
        return user
    
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
                next_url = request.GET.get('next')
                if next_url:
                    return HttpResponseRedirect(next_url)
                else:
                    return render(request,self.template_name, context={'message': f'Bienvenido {user}'})
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
    
class Registerview(TemplateView):
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
 
class EditarView(LoginRequiredMixin, UpdateView):#FUNCIONA
    model = User#modelo a usar
    template_name = 'forms/editar.html'#direccion url para editar
    success_url = "/"#
    fields = ['username', 'password']#campos que interactuan al momento de editarF
    initial = {'username':''}#inicializa los campos en blanco
    initial = {'password':''}#inicializa los campos en blanco

class borrarview(DeleteView):#FUNCIONA
    
    model = User#modelo del curso 
    template_name = 'forms/borrar.html'#direccion url para borrar
    success_url = "/"#donde nos redirecciona si se logra crear el curso PF NO ME MUESTRA EL MENSAJE PERO SI AGREGA LOS DATOS 
    
class EntradaView(TemplateView):
    model = Entrada#modelo a usar
    template_name = 'forms/entrada.html'#direccion url para la entrada
    success_url = "/"#
    fields = ['titulo', 'password', 'subtitulo', 'fecha']#campos que interactuan al momento de crear un post
  
class MensajeriaView(CreateView):
    model = Mensaje#modelo a usar
    template_name = 'forms/mensajeria.html'#direccion url para la entrada
    fields = ['para', 'mensaje', 'fecha',]#campos que interactuan al momento de crear un post
    success_url = "/mensajeria"#
    def form_valid(self, form):
            self.object = form.save()
            self.object.de = self.request.user
            self.object.save()
            return HttpResponseRedirect(self.get_success_url())

class UsuariosViews(TemplateView):
    Mostrar = 'forms/usuario.html'
    def get(self, request, status=None):#Envia informacion 
        context = {
            'elements': User.objects.filter().order_by('username')
        }
        return render(request, self.Mostrar, context)
    pass