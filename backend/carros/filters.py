import django_filters
from .models import Carros

class CarroFilter(django_filters.FilterSet):
    marca=django_filters.CharFilter(lookup_expr='icontains')
    ano_gt=django_filters.NumberFilter(field_name='ano',lookup_expr='gt')
    ano_lt=django_filters.NumberFilter(field_name='ano',lookup_expr='lt')
    preco_gt=django_filters.NumberFilter(field_name='preco',lookup_expr='gt')
    preco_lt=django_filters.NumberFilter(field_name='preco',lookup_expr='lt')
    class Meta:
        model = Carro
        fields= ['categoria','ano','cambio']