from django.shortcuts import render
from .models import Carro
from .filters import CarroFilter
# Create your views here.

def index(request):
    novos_carros = Carro.objects.filter(categoria="Novo")[:6]
    carros_usados = Carro.objects.filter(categoria="Usado")[:6]
    ultimos_carros =Carro.objects.all().order_by('-date')[:5]
    all = Carro.objects.all()
    myFilter = CarroFilter(request.GET,queryset=all)
    all = myFilter.qs
    context = {
        "carros_novos": carros_novos,
        "carros_usados": carros_usados,
        "ultimos_carros": ultimos_carros,
        "all":all,
        "myFilter":myFilter
    }

    return render(request, 'index.html',context)

def filter_results(request):
    all = Carro.objects.all()
    myFilter = CarroFilter(request.GET,queryset=all)
    all = myFilter.qs

    context={
        'all':all,
        'myFilter':myFilter
    }

    return render(request, 'filter_results.html',context)