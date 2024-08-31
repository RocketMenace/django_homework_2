from django.core.management import BaseCommand
from catalog.models import Product, Category
import json


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        try:
            with open("catalog/fixtures/catalog_data.json", "r") as file:
                content = json.load(file)
                return [x for x in content if x["model"] == "catalog.category"]
        except FileNotFoundError as err:
            (print(f"The {err} is  occurred."))

    @staticmethod
    def json_read_products():
        try:
            with open("catalog/fixtures/catalog_data.json", "r") as file:
                content = json.load(file)
                return [x for x in content if x["model"] == "catalog.product"]
        except FileNotFoundError as err:
            print(f"The {err} is  occurred.")

    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()
        product_fot_create = []
        category_for_create = []

        for category in Command.json_read_categories():
            category_for_create.append(Category(category["pk"], **category["fields"]))

        Category.objects.bulk_create(category_for_create)

        for product in Command.json_read_products():
            product_fot_create.append(
                Product(product["pk"],
                        product["fields"]["name"],
                        product["fields"]["description"],
                        product["fields"]["slug"],
                        product["fields"]["image"],
                        product["fields"]["category"],
                        product["fields"]["price"],
                        product["fields"]["created_at"],
                        product["fields"]["updated_at"],
                        product["fields"]["currency"]))

        Product.objects.bulk_create(product_fot_create)
