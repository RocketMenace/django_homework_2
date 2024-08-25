from django.shortcuts import render


# Create your views here.


def get_home_page(request):
    return render(request, "home.html")


def get_contacts_page(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        print(f"{name} {phone} {message}")
    return render(request, "contacts.html")
