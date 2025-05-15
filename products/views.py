from django.http import HttpResponse
from django.shortcuts import render
from .models import Product, Category

# Create your views here.
def salom(request):
    return HttpResponse("Salom")

def info(request, category, name):
    ans = f"{category}/{name}"
    product = Product.objects.select_related('category').get(name=name)
    return HttpResponse(f"{product.name} - {product.price}")