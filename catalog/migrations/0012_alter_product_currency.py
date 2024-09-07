# Generated by Django 5.1 on 2024-09-07 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0011_alter_product_currency"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="currency",
            field=models.CharField(
                choices=[("RUB", "Rubles"), ("USD", "Dollars")],
                default="USD",
                max_length=3,
            ),
        ),
    ]
