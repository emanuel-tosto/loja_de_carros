from django.db import models

# Create your models here.
class Vendedor(models.Model):
    nome = models.CharField(max_length=50)
    foto = models.ImageField(upload_to='images')
    descricao = models.TextField()
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
