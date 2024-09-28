from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, TemplateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.forms import inlineformset_factory
from django_countries import settings
from django.core.cache import cache
from .models import Product, Category, Version
from .forms import ProductCreateForm, ProductUpdateForm, VersionUpdateForm, ProductOwnerForm, ProductModeratorForm
from .services import get_categories


# Create your views here.


class ProductListView(ListView):
    model = Product
    queryset = Product.active.all()
    paginate_by = 2
    template_name = "home.html"
    context_object_name = "products"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["versions"] = Version.objects.all().filter(is_active=True)
        return context


class ContactsTemplateView(TemplateView):
    template_name = "contacts.html"


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = "product.html"
    login_url = reverse_lazy("users:login")
    redirect_field_name = reverse_lazy("catalog:product_list")

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        if settings.CACHE_ENABLED:
            key = f"product_{self.object.pk}"
            product = cache.get(key)
            if product is None:
                product = Product.objects.get(pk=self.object.pk)
                cache.set(key, product, 30)
        else:
            product = Product.objects.get(pk=self.object.pk)
        context_data["product"] = product
        return context_data

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductCreateForm
    template_name = "add_product.html"
    success_url = reverse_lazy("catalog:product_list")
    login_url = reverse_lazy("users:login")
    redirect_field_name = reverse_lazy("catalog:product_list")

    def get_context_data(self, **kwargs):
        SubjectFormSet = inlineformset_factory(Product, Version, form=VersionUpdateForm, extra=1)
        context = super(ProductCreateView, self).get_context_data()
        context["categories"] = Category.objects.all()
        context["formset"] = SubjectFormSet
        if self.request.method == "POST":
            context["formset"] = SubjectFormSet(self.request.POST)
        else:
            context["formset"] = SubjectFormSet()
            context["versions"] = Version.objects.all()
        return context

    def form_valid(self, form):
        formset = self.get_context_data()["formset"]
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.instance.owner = self.request.user
            formset.save()

        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductUpdateForm
    success_url = reverse_lazy("catalog:product_list")
    template_name = "edit_product.html"
    login_url = reverse_lazy("users:login")
    redirect_field_name = reverse_lazy("catalog:product_list")

    def get_context_data(self, **kwargs):
        SubjectFormSet = inlineformset_factory(Product, Version, form=VersionUpdateForm, extra=1)
        context = super(ProductUpdateView, self).get_context_data()
        context["categories"] = Category.objects.all()
        context["formset"] = SubjectFormSet
        if self.request.method == "POST":
            context["formset"] = SubjectFormSet(self.request.POST, instance=self.object)
        else:
            context["formset"] = SubjectFormSet(instance=self.object)
        return context

    def form_valid(self, form):
        formset = self.get_context_data()["formset"]
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)

    def get_form_class(self):
        user = self.request.user
        if user.is_superuser:
            return ProductUpdateForm
        if user == self.object.owner:
            return ProductOwnerForm
        if user.is_moderator:
            return ProductModeratorForm
        raise PermissionDenied("Не хватает прав доступа. Обратитесь к администратору")


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:product_list")
    template_name = "product_confirm_delete.html"
    login_url = reverse_lazy("users:login")
    redirect_field_name = reverse_lazy("catalog:product_list")


class CategoryListView(LoginRequiredMixin,ListView):
    model = Category
    login_url = reverse_lazy("users:login")
    redirect_field_name = reverse_lazy("catalog:product_list")
    context_object_name = "categories"
    paginate_by = 4
    template_name = "categories.html"

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        if settings.CACHE_ENABLED:
            key = f"categories_{self.object_list}"
            categories = cache.get(key)
            if categories is None:
                categories = get_categories()
                cache.set(key, categories)
        else:
            categories = get_categories()
        context_data["categories"] = categories
        return context_data

def products_by_category(request, pk):
    products = Category.objects.get(pk=pk).products.all().filter(status="Активен")
    return render(request, "home.html", {"products": products})