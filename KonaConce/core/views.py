from django.shortcuts import render,HttpResponse

def home(request):
    return render(request,"core/home.html")

def QuienesSomos(request):
    return render(request,"core/quienes_somos.html")

def FAQ(request):
    return render(request,"core/faq.html")

def galeria(request):
    return render(request,"core/galeria_kona.html")

    return render(request, "error404/404.html", status=404)

