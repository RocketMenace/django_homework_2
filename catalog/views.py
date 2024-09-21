from django.views.generic import CreateView, ListView, DetailView, TemplateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.forms import inlineformset_factory
from .models import Product, Category, Version
from .forms import ProductCreateForm, ProductUpdateForm, VersionUpdateForm


# Create your views here.


class ProductListView(ListView):
    model = Product
    paginate_by = 2
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["versions"] = Version.objects.all().filter(is_active=True)
        return context


class ContactsTemplateView(TemplateView):
    template_name = "contacts.html"


class ProductDetailView(DetailView):
    model = Product
    template_name = "product.html"


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductCreateForm
    template_name = "add_product.html"
    success_url = reverse_lazy("catalog:product_list")

    def get_context_data(self, **kwargs):
        SubjectFormSet = inlineformset_factory(Product, Version, form=VersionUpdateForm, extra=1)
        context = super(ProductCreateView, self).get_context_data()
        context["categories"] = Category.objects.all()
        context["formset"] = SubjectFormSet
        if self.request.method == "POST":
            context["formset"] = SubjectFormSet(self.request.POST)
        else:
            context["formset"] = SubjectFormSet()
        return context

    def form_valid(self, form):
        formset = self.get_context_data()["formset"]
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductUpdateForm
    success_url = reverse_lazy("catalog:product_list")
    template_name = "edit_product.html"

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


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:product_list")
    template_name = "product_confirm_delete.html"
