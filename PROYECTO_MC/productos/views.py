from django.shortcuts import render
from .models import producto
# Create your views here.
def productos(request):
    products = producto.objects.all()
    return render(request,"PRODUCTOS/productos.html", {'products':products});