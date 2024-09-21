from django.forms import ModelForm, ValidationError, BooleanField
from .models import Product, Version

FORBIDDEN_WORDS = "казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция", "радар"


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs["class"] = "form-check-input"
            else:
                field.widget.attrs["class"] = "form-control"


class ProductUpdateForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "image", "price", "category", "currency"]

    def clean_name(self):
        data = self.cleaned_data["name"]
        for word in FORBIDDEN_WORDS:
            if word in data:
                raise ValidationError("Указано запрещенное имя.", code="invalid")
        return data

    def clean_description(self):
        data = self.cleaned_data["description"]
        for word in FORBIDDEN_WORDS:
            if word in data:
                raise ValidationError("Указано запрещенное описание.", code="invalid")
        return data


class ProductCreateForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "image", "price", "category", "currency"]

    def clean_name(self):
        data = self.cleaned_data["name"]
        for word in FORBIDDEN_WORDS:
            if word in data:
                raise ValidationError("Указано запрещенное имя.", code="invalid")
        return data

    def clean_description(self):
        data = self.cleaned_data["description"]
        for word in FORBIDDEN_WORDS:
            if word in data:
                raise ValidationError("Указано запрещенное описание.", code="invalid")
        return data


class VersionUpdateForm(StyleFormMixin, ModelForm, ):
    class Meta:
        model = Version
        fields = "__all__"

    # def clean_is_active(self, pk):
    #     product = Product.objects.
    #     versions = product.versions.all()
    #     data = self.cleaned_data["is_active"]
    #     for version in versions:
    #         if version.is_active and data:
    #             raise ValidationError("Можно указать только одну версию")
    #     return data
