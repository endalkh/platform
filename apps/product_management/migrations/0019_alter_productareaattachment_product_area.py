# Generated by Django 4.2.2 on 2024-03-28 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        (
            "product_management",
            "0018_productareaattachment_delete_capabilityattachment",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="productareaattachment",
            name="product_area",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="attachments",
                to="product_management.productarea",
            ),
        ),
    ]
