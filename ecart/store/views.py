from django.shortcuts import render
from . models import Product

# Create your views here.

def home(req):
    return render(req,'index.html')


def store_page(req):
    Products = Product.objects.all()
    return render(req,'store/products.html',{ 'Products':Products })