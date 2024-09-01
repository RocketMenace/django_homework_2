from django.urls import path
from .views import get_home_page, get_contacts_page, show_product

urlpatterns = [
    path("", get_home_page, name="home"),
    path("contacts/", get_contacts_page, name="contacts"),
    path("product/<int:pk>/", show_product, name="product")
]
