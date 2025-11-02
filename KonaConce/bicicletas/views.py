from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Bike, Categoria

def bike_list(request):
    categoria_id = request.GET.get('categoria')
    categorias = Categoria.objects.all()
    bike_list = Bike.objects.select_related('marca', 'categoria')

    if categoria_id:
        bike_list = bike_list.filter(categoria__id=categoria_id)

    bike_list = bike_list.order_by("-created")
    paginator = Paginator(bike_list, 4)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'categorias': categorias,
        'categoria_id_seleccionada': int(categoria_id) if categoria_id else None
    }
    
    return render(request, "bicicletas/bike_list.html", context)


def bike_detail(request, pk):
    """
    Vista para el detalle de una bicicleta.
    Optimizada con select_related.
    """
    bike = get_object_or_404(
        Bike.objects.select_related('marca', 'categoria'), 
        pk=pk
    )
    return render(request, "bicicletas/bike_detail.html", {"bike": bike})