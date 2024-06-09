from django.shortcuts import render , get_object_or_404
from . models import Product

# Create your views here.

def home(req):
    return render(req,'index.html')


def store_page(req):
    Products = Product.objects.all()
    return render(req,'store/store.html',{ 'Products':Products })

def products(req, pk):
    Products = Product.objects.get(id=pk)
    return render(req,'store/Product.html',{ 'Product':Products })