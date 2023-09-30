from django.shortcuts import render,get_list_or_404
#from django.http import request
from .models import Product, Category

# Create your views here.

def categories(request):
    return{'categories': Category.objects.all()}

def all_products(request):
    products = Product.objects.all()
    return render(request, 'store/home.html', {'products':products})

def product_detail(request, slug):
    product = get_list_or_404(Product, slug=slug, in_stock=True)