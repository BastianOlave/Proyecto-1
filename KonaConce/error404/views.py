from django.shortcuts import render

def pagina_404_view(request):
    return render(request, "error404/404.html", status=404)