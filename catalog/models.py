from django.db import models
from users.models import User
# Create your models here.


NULLABLE = {"blank": True, "null": True}


class ProductStatusManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(status=Product.Status.ACTIVE)

class Contact(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="first_name")
    last_name = models.CharField(max_length=50, verbose_name="last_name")
    email = models.EmailField(max_length=50)
    phone_number = models.CharField(max_length=12)

    class Meta:
        verbose_name = "contact"
        verbose_name_plural = "contacts"
        ordering = ["last_name"]


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="название")
    description = models.TextField(verbose_name="описание")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"
        ordering = ["name"]
        indexes = [models.Index(fields=["name", ])]


class Product(models.Model):
    class Currency(models.Choices):
        RUBLES = "RUB"
        DOLLARS = "USD"

    class Status(models.TextChoices):
        ACTIVE = "Активен"
        NOT_ACTIVE = "Не активен"

    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="владелец", related_name="owner", **NULLABLE)
    name = models.CharField(max_length=50, verbose_name="название")
    description = models.TextField(verbose_name="описание")
    slug = models.SlugField(max_length=100, default="product", **NULLABLE)
    image = models.ImageField(upload_to="products/", verbose_name="изображение", **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products", verbose_name="категория")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="цена")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    currency = models.CharField(max_length=3, choices=Currency.choices, default=Currency.DOLLARS, verbose_name="валюта")
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.NOT_ACTIVE, verbose_name="статус")
    objects = models.Manager()
    active = ProductStatusManager()

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = ["name", "price"]
        indexes = [models.Index(fields=["name", ])]
        permissions = [("set_status", "Can change product status"),
                       ("change_product_description", "Can change product description"),
                       ("change_product_category", "Can change product category")]


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="продукт", related_name="versions")
    version_number = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="версия")
    version_name = models.CharField(max_length=50, verbose_name="имя версии")
    is_active = models.BooleanField(default=False, verbose_name="Активный статус")

    class Meta:
        verbose_name = "версия"
        verbose_name_plural = "версии"

    def __str__(self):
        return f"{self.version_name}"
