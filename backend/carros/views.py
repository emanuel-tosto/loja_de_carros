from django.shortcuts import render,get_object_or_404
from .models import Carro
from .filters import CarroFilter
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
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
    page = request.GET.get('page')
    paginator = Paginator(all,1)
    try:
        all=paginator.page(page)
    except PageNotAnInteger:
        all = paginator.page('1')
    except EmptyPage:
        all = paginator.page(paginator.num_pages)
    page_obj=paginator.get_page(page)

    context={
        'all':all,
        'myFilter':myFilter
        'page_obj':page_obj
    }

    return render(request, 'filter_results.html',context)

def carro_detail(request,carro_id):
    carros = get_object_or_404(Carro, id=carro_id)
    context={
        'carros': carros
        }    
    return render(request,'car_detail.html',context)