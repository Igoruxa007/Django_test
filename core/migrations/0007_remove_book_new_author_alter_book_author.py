# Generated by Django 5.1.6 on 2025-04-19 18:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0006_book_new_author"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="book",
            name="new_author",
        ),
        migrations.AlterField(
            model_name="book",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="core.author"
            ),
        ),
    ]
