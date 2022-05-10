from django.test import TestCase
from proyecto_final.muestro.models import Entrada

class EntradaTestCase(TestCase):
    def test_create_entrada(self):
        entrada = Entrada.objects.create(
            titulo = 'Esto es una prueba del titulo con unittest',
            mensaje= 'Esto es una prueba del mensaje con unittest',
            subtitulo= 'Esto es una prueba del subtitulo con unittest'
            
        )
        assert isinstance(entrada, Entrada)
        assert Entrada.objects.filter(id=entrada.id).exist
        assert entrada.titulo == 'Esto es una prueba del titulo con unittest'