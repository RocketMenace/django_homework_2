# Generated by Django 4.2 on 2024-09-25 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_alter_user_avatar"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="is_moderator",
            field=models.BooleanField(default=False),
        ),
    ]
