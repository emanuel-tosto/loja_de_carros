from rest_framework import serializers
from vendedores.models import Vendedor

class VendedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendedor
        fields = ('nome','foto','descricao','email')