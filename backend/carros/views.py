from django.shortcuts import render,get_object_or_404
from .models import Carro
from .filters import CarroFilter
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
from vendedores.models import Vendedor
# Create your views here.
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from carros.serializers import CarroSerializer
@csrf_exempt
def index(request):
    carros_novos = Carro.objects.filter(categoria="Novo")[:6]
    carros_usados = Carro.objects.filter(categoria="Usado")[:6]
    ultimos_carros =Carro.objects.all().order_by('preco')[:5]
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

def about(request):
    return render(request,'about.html')

def filter_results(request):
    all = Carro.objects.all()
    myFilter = CarroFilter(request.GET,queryset=all)
    all = myFilter.qs
    page = request.GET.get('page')
    paginator = Paginator(all,5)
    try:
        all=paginator.page(page)
    except PageNotAnInteger:
        all = paginator.page('1')
    except EmptyPage:
        all = paginator.page(paginator.num_pages)
    
    page_obj=paginator.get_page(page)

    context={
        'all':all,
        'myFilter':myFilter,
        'page_obj':page_obj
    }

    return render(request, 'filter_results.html',context)

def carro_detail(request,carro_id):
    carros = get_object_or_404(Carro, id=carro_id)
    context={
        'carros': carros
        }    
    return render(request,'car_detail.html',context)


def inventory(request):
    inventory_cars = Carro.objects.all().order_by('preco')
    #carro_serializer = CarroSerializer(inventory_cars,many=True)
    page = request.GET.get('page')
    paginator = Paginator(inventory_cars,5)
    try:
        all=paginator.page(page)
    except PageNotAnInteger:
        all = paginator.page('1')
    except EmptyPage:
        all = paginator.page(paginator.num_pages)
    
    page_obj=paginator.get_page(page)
    context = {
        'inventory_cars': inventory_cars,
        'page_obj':page_obj
    }

    return render(request,'inventory.html',context)#JsonResponse(carro_serializer.data,safe=False)

def vendedores(request):
    all_vendedores = Vendedor.objects.all()
    context = {
        'all_vendedores':all_vendedores
    }

    return render(request,'vendedores.html',context)

def contact(request):
    return render(request,'contact.html')