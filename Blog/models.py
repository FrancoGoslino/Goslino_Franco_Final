from django.db import models
from django.contrib.auth.models import User

class Receta(models.Model):
    nombre = models.CharField(max_length=100)
    detalle = models.TextField(max_length=1000)
    precio = models.FloatField()
    imagen = models.ImageField(upload_to="menues", null=True, blank=True)
    propietario = models.ForeignKey(to=User, on_delete=models.CASCADE , related_name="propietario")

    @property
    def image_url(self):
        return self.imagen.url if self.imagen else ''
    
    def __str__(self):
        return f"{self.id} - {self.nombre} - {self.propietario.id}"

class Mensaje(models.Model):
    mensaje = models.TextField(max_length=100)
    email = models.EmailField()
    creado_el = models.DateTimeField(auto_now_add=True) 
    destinatario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="mensajes")
    

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="perfil")
    avatar = models.ImageField(upload_to="avatares", null=True, blank=True)
    redes_sociales = models.CharField(max_length=50)

    @property
    def avatar_url(self):
        return self.avatar.url if self.avatar else ''