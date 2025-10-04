from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Bike
from django.shortcuts import render, get_object_or_404

def bike_list(request):
    bikes = Bike.objects.all().order_by("-created")
    paginator = Paginator(bikes, 4)  # 4 bicis
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "bicicletas/bike_list.html", {"page_obj": page_obj})

def bike_detail(request, pk):
    bike = get_object_or_404(Bike, pk=pk)
    return render(request, "bicicletas/bike_detail.html", {"bike": bike})
