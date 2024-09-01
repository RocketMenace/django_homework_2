from django.shortcuts import render
from .models import Product


# Create your views here.


def get_home_page(request):
    products = Product.objects.all()
    context = {"products": products, }
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
