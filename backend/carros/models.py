from django.db import models
import datetime
from vendedores.models import Vendedor
# Create your models here.

class Carro(models.Model):
    vendedor = models.ForeignKey(Vendedor,on_delete=models.DO_NOTHING)
    marca = models.CharField(max_length=100)
    CATEGORIA = (("Novo","Novo"),
                ("Usado","Usado"))
    categoria= models.CharField(max_length=50, choices=CATEGORIA)
    image_main = models.ImageField(upload_to='images', blank=True)
    image1 = models.ImageField(upload_to='images', blank=True)
    image2 = models.ImageField(upload_to='images', blank=True)
    image3 = models.ImageField(upload_to='images', blank=True)
    image4 = models.ImageField(upload_to='images', blank=True)
    image5 = models.ImageField(upload_to='images', blank=True)

    milhagem= models.IntegerField(blank=True, null=True)
    CAMBIO=(
        ('Manual','Manual'),
        ('Automatico','Automatico')
    )
    CAMBIO = models.CharField(max_length=50,choices=CAMBIO)
    ANO_ESCOLHAS = [(r,r) for r in range(2005,datetime.date.today().year+1)]
    ano = models.IntegerField(('year'),choices=ANO_ESCOLHAS,default=datetime.datetime.now().year)
    forca= models.IntegerField()
    combustivel=models.IntegerField()
    preco = models.IntegerField()
    descricao = models.TextField()
    data = models.DateField()

    def __str__(self):
        return self.marca
