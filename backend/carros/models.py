from django.db import models
import datetime
from vendedores.models import Vendedor
# Create your models here.

class Car(models.Model):
    vendedor = models.ForeignKey(Vendedor,on_delete=models.DO_NOTHING)
    marca = models.CharField(max_length=100)
    CATEGORIA = (("Novo","Novo"),
                ("Usado","Usado"))
    categoria= models.CharField(max_length=50, choices=CATEGORia)
    image_main = models.ImageField(upload_to='images', blank=True)
    image1 = models.ImageField(upload_to='images', blank=True)
    image2 = models.ImageField(upload_to='images', blank=True)
    image3 = models.ImageField(upload_to='images', blank=True)
    image4 = models.ImageField(upload_to='images', blank=True)
    image5 = models.ImageField(upload_to='images', blank=True)

    milhagem= models.IntegerField(blank=true, null=True)
    TRANSMISSAO=(
        ('Manual','Manual'),
        ('Automatica','Automatica')
    )
    transmissao = models.CharField(max_length=50,choices=TRANSMISSAO)
    ANO_ESCOLHAS = [(r,r) for r in range(2005,datetime.date.today().year+1)]
    ano = models.IntegerField(('year'),choices=YEAR_CHOICES,default=datetime.now().year)
    forca= models.IntegerField()
    combustivel=models.IntegerField()
    preco = models.IntegerField()
    descricao = models.TextField()
    data = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.marca