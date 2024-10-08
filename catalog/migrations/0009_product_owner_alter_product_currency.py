# Generated by Django 4.2 on 2024-09-23 12:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("catalog", "0008_alter_product_currency"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="owner",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="owner",
                to=settings.AUTH_USER_MODEL,
                verbose_name="владелец",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="currency",
            field=models.CharField(
                choices=[("RUB", "Rubles"), ("USD", "Dollars")],
                default="USD",
                max_length=3,
                verbose_name="валюта",
            ),
        ),
    ]
