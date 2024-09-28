from django.urls import path
from .views import (
    ProductListView,
    ProductDetailView,
    ProductCreateView,
    ContactsTemplateView,
    ProductUpdateView,
    ProductDeleteView,
    CategoryListView,
    products_by_category,
)

app_name = "catalog"

urlpatterns = [
    path("", ProductListView.as_view(), name="product_list"),
    path("categories/>", CategoryListView.as_view(), name="categories_list"),
    path(
        "categories_products/<int:pk>/",
        products_by_category,
        name="categories_products",
    ),
    path("add_products/", ProductCreateView.as_view(), name="add_product"),
    path("edit_product/<int:pk>", ProductUpdateView.as_view(), name="edit_product"),
    path("delete_product/<int:pk>", ProductDeleteView.as_view(), name="delete_product"),
    path("page/<int:page>", ProductListView.as_view(), name="paginator"),
    path("product/<int:pk>/", ProductDetailView.as_view(), name="product"),
    path("contacts/", ContactsTemplateView.as_view(), name="contacts"),
]
