# Generated by Django 4.2.2 on 2024-05-13 09:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("product_management", "0026_idea_voted_users"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="idea",
            name="vote_count",
        ),
    ]
