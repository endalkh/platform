# Generated by Django 4.2.2 on 2024-05-14 12:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("security", "0005_ideavote"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ideavote",
            name="voter",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
