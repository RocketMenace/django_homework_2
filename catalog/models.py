from django.db import models

# Create your models here.


NULLABLE = {"blank": True, "null": True}


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
    name = models.CharField(max_length=50, verbose_name="name")
    description = models.TextField(verbose_name="description")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"
        ordering = ["name"]
        indexes = [models.Index(fields=["name", ])]


class Product(models.Model):
    class Currency(models.Choices):
        RUBLES = "RUB"
        DOLLARS = "USD"

    name = models.CharField(max_length=50, verbose_name="name")
    description = models.TextField(verbose_name="description")
    slug = models.SlugField(max_length=100)
    image = models.ImageField(upload_to="products/", verbose_name="image", **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    currency = models.CharField(max_length=3, choices=Currency.choices, default=Currency.DOLLARS)

    # manufactured_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "product"
        verbose_name_plural = "products"
        ordering = ["name", "price"]
        indexes = [models.Index(fields=["name", ])]
