# Generated by Django 4.1.7 on 2023-04-01 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Blog",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100, verbose_name="Title")),
                ("text", models.TextField(verbose_name="text")),
                ("date_created", models.DateField(auto_now_add=True)),
                ("date_updated", models.DateField(auto_now=True)),
                ("is_published", models.BooleanField()),
                ("image", models.ImageField(upload_to="")),
            ],
            options={
                "verbose_name": "Blog",
                "verbose_name_plural": "Blogs",
                "ordering": ["id"],
            },
        ),
    ]