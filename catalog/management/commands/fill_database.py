from django.core.management import BaseCommand
import json

class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        try:
            with open("catalog/fixtures/catalog_data.json", "r") as file:
                content = json.load(file)
                # return [x for x in content if x["model"] == "catalog.category"]
                print([x for x in content if x["model"] == "catalog.category"])
        except FileNotFoundError as err:
            print(f"The {err} is  occurred.")






    def handle(self, *args, **options):
        Command.json_read_categories()
