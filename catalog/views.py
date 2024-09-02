from django.shortcuts import render
from .models import Product, Category
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


def add_product(request):
    categories = Category.objects.all()
    context = {"categories": categories}
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        image = request.POST.get("image")
        price = request.POST.get("price")
        category = request.POST.get("category")
        category_id = Category.objects.get(id=category)
        currency = request.POST.get("currency")
        product = Product(name=name, description=description, image=image, price=price, category=category_id,
                          currency=currency)
        product.save()
    return render(request, "add_product.html", context)
