from django.shortcuts import render
from .models import Product

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def info(request):
    productCount = Product.objects.count()
    return render(request, 'info.html', {'productCount': productCount})

def index(request):
    return render(request, 'index.html')

def product_details(request, product_id):
    product = Product.objects.filter(id=product_id).first()
    return render(request, 'product_details.html', {'product': product})
