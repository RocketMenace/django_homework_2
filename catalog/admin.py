from django.contrib import admin
from .models import Product, Category, Contact


# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "currency", "category", "created_at")
    list_filter = ("category",)
    search_fields = ("name", "description")
    prepopulated_fields = {"slug": ("name",)}
    raw_id_fields = ["category"]
    date_hierarchy = "created_at"
    ordering = ["name"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "email", "phone_number")
    list_filter = ("first_name", "last_name")
    search_fields = ("first_name", "last_name", "email", "phone_number")
    ordering = ("first_name", "last_name")
