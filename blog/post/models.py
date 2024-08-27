from django.db import models

# Create your models here.
class Post(models.Model):
    titulo = models.CharField(max_length= 200)
    contenido = models.TextField()
    fecha_publicacion = models.DateField()
    categoria = models.CharField(max_length= 200)
    autor = models.CharField(max_length= 200)

    def __str__(self):
        return  self.titulo
