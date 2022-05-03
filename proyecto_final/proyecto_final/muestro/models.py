#creo los modelos de la base de datos 
from asyncio.proactor_events import _ProactorBaseWritePipeTransport
from pyexpat import model
from django.db import models
from django.db.models import Model

class Usuario(models.Model):
    user=models.CharField(max_length=250)
    password=models.CharField(max_length=250)
    mail=models.EmailField( max_length=254)
    is_admin=models.BooleanField(default=False)
    def __str__(self):
        return f"{self.user}"
    
class Entrada(models.Model):
    titulo=models.CharField(max_length=250)
    mensaje=models.TextField()
    fecha=models.DateTimeField()
    autor=models.ForeignKey(Usuario, on_delete = models.CASCADE, related_name = "autor", blank=True, null=True)
    subtitulo=models.CharField(max_length=250)
    imagen=models.ImageField()
    
class Mensaje(models.Model):
    de=models.ForeignKey(Usuario, on_delete = models.CASCADE, related_name = "de", blank=True, null=True)
    para=models.ForeignKey(Usuario, on_delete = models.CASCADE, related_name = "para", blank=True, null=True)
    mensaje=models.CharField(max_length=250)
    fecha=models.DateTimeField()
    
# entradas(posts) titulo, mensaje, fecha, autor, subtitulo, imagen
# mensajes (messages) de, para, mensaje, fecha_de_creado