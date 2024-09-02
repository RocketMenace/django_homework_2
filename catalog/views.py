from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator


# Create your views here.


def get_home_page(request, page_number=1):
    products = Product.objects.all()
    paginator = Paginator(products, per_page=2)
    products_paginator = paginator.page(page_number)
    context = {"products": products_paginator, }
    return render(request, "home.html", context)


def get_contacts_page(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        print(f"{name} {phone} {message}")
    return render(request, "contacts.html")


def show_product(request, pk):
    product = Product.objects.get(pk=pk)
    context = {"product": product}
    return render(request, "product.html", context)
