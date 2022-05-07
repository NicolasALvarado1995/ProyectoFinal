from django.contrib import admin
from .models import *
#este archivo genera el admin de django
admin.site.register(Entrada)
admin.site.register(Mensaje)
