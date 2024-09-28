from .models import Category

def get_categories():
    categories = Category.objects.all()
    return categories