from django.urls import path
from .views import ProductListView, ProductDetailView, ProductCreateView, ContactsTemplateView

app_name = "catalog"

urlpatterns = [
    path("", ProductListView.as_view(), name="product_list"),
    path("add_products/", ProductCreateView.as_view(), name="add_product"),
    path("page/<int:page>", ProductListView.as_view(), name="paginator"),
    path("product/<int:pk>/", ProductDetailView.as_view(), name="product"),
    path("contacts/", ContactsTemplateView.as_view(), name="contacts")

]
