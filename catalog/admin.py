from django.contrib import admin
from .models import Product, Category, Contact, Version


# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "owner","currency", "category", "created_at")
    list_filter = ("category", "owner")
    search_fields = ("name", "description", "owner")
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


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ["product_id", "version_number", "version_name", "is_active"]
    list_filter = ["version_number", "version_name", "is_active"]
    ordering = ["-version_number"]
