from django.db import models

class Autor(models.Model):
    nombre= models.CharField(max_length=100)
    apellido= models.CharField(max_length=100)
    fecha_nacimiento= models.DateField()
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
        
class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    fecha_publi = models.DateField()
    genero = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13,unique=True)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.titulo
