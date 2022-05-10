#creo los modelos de la base de datos
from django.db import models
from proyecto_final.users.models import User

class Entrada(models.Model):
    titulo=models.CharField(max_length=250)
    mensaje=models.TextField()
    fecha=models.DateTimeField()
    autor=models.ForeignKey(User, on_delete = models.CASCADE, related_name = "autor", blank=True, null=True)
    subtitulo=models.CharField(max_length=250)
    imagen=models.ImageField()
    
class Mensaje(models.Model):
    de=models.ForeignKey(User, on_delete = models.CASCADE, related_name = "de", blank=True, null=True)
    para=models.ForeignKey(User, on_delete = models.CASCADE, related_name = "para", blank=True, null=True)
    mensaje=models.CharField(max_length=250)
    fecha=models.DateTimeField()
    
class avatar(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="avatar", null=True, blank=True)
    