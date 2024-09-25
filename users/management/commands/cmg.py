from django.core.management import BaseCommand
from django.contrib.auth.models import Group, Permission

from blog.urls import app_name
from catalog.models import Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        group = Group.objects.create(name="Moderator")
        set_status = Permission.objects.get(codename="set_status")
        change_product_description = Permission.objects.get(codename="change_product_description")
        change_product_category = Permission.objects.get(codename="change_product_category")
        group.permissions.add(set_status, change_product_description, change_product_category)
        group.save()
