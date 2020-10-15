from django.shortcuts import render

# Create your views here

from .forms import *
from .models import Product


def product_create_view(request):
    form = RawProductForm()
    if request.method == "POST":
        form = RawProductForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            Product.objects.create(**form.cleaned_data)
        else:
            print(form.errors)
    
    context = {
        'form': form
    }
    return render(request, "product/create.html", context)

def product_detail_view(request):
    obj = Product.objects.get(id=1)
    context = {
        'obj': obj
    }
    return render(request, "product/detail.html", context)