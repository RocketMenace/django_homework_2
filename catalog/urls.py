from django.urls import path
from .views import get_home_page, get_contacts_page, show_product

urlpatterns = [
    path("", get_home_page, name="home"),
    path("page/<int:page_number>", get_home_page, name="paginator"),
    path("contacts/", get_contacts_page, name="contacts"),
    path("product/<int:pk>/", show_product, name="product")
]

# app_name = "catalog"