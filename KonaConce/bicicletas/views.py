from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
# Importamos Categoria y Bike
from .models import Bike, Categoria

def bike_list(request):
    """
    Vista para listar todas las bicicletas, con paginación
    y filtrado por categoría (Punto 4).
    """
    
    # 1. Obtenemos el ID de la categoría desde la URL (ej: ?categoria=1)
    categoria_id = request.GET.get('categoria')
    
    # 2. Obtenemos todas las categorías para mostrarlas como botones
    categorias = Categoria.objects.all()

    # 3. Filtramos las bicicletas
    # Optimizamos la consulta con select_related para cargar marca y categoría
    bike_list = Bike.objects.select_related('marca', 'categoria')

    if categoria_id:
        # Si se seleccionó una categoría, filtramos el queryset
        bike_list = bike_list.filter(categoria__id=categoria_id)
    
    # Mantenemos el orden
    bike_list = bike_list.order_by("-created")

    # 4. Paginamos el queryset (ya sea completo o filtrado)
    paginator = Paginator(bike_list, 4)  # 4 bicis por página
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    # 5. Pasamos todo al contexto
    context = {
        'page_obj': page_obj,
        'categorias': categorias, # La lista de botones de filtro
        'categoria_id_seleccionada': int(categoria_id) if categoria_id else None # Para saber qué botón marcar como "activo"
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