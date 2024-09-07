from django.views.generic import CreateView, ListView, DetailView, TemplateView
from django.urls import reverse_lazy
from .models import Product, Category


# Create your views here.


class ProductListView(ListView):
    model = Product
    paginate_by = 2
    template_name = "home.html"


class ContactsTemplateView(TemplateView):
    template_name = "contacts.html"


class ProductDetailView(DetailView):
    model = Product
    template_name = "product.html"


class ProductCreateView(CreateView):
    model = Product
    template_name = "add_product.html"
    fields = ["name", "description", "image", "price", "category", "currency"]
    success_url = reverse_lazy("catalog:product_list")

    def get_context_data(self, **kwargs):
        context = super(ProductCreateView, self).get_context_data()
        context["categories"] = Category.objects.all()
        return context
