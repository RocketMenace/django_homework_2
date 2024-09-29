from django.core.cache import cache
from django_countries import settings
from .models import Category


def get_categories():
    if settings.CACHE_ENABLED:
        key = "cached_categories"
        categories = cache.get(key)
        if categories is None:
            categories = Category.objects.all()
            cache.set(key, categories, 10)
    else:
        categories = Category.objects.all()
    return categories
