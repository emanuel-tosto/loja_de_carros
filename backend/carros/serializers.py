from rest_framework import serializers
from carros.models import Carro

class CarroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carro
        fields = ('vendedor','marca','categoria','image_main',
        'image1','image2','image3','image4','image5','milhagem',
        'cambio','ano','forca','combustivel','preco','descricao','data')