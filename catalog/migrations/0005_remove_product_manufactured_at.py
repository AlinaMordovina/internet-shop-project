# Generated by Django 5.0.2 on 2024-02-17 16:45

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("catalog", "0004_product_manufactured_at"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="manufactured_at",
        ),
    ]
