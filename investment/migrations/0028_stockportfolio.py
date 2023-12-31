# Generated by Django 4.1.7 on 2023-05-19 16:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("investment", "0027_remove_news_banner_image"),
    ]

    operations = [
        migrations.CreateModel(
            name="StockPortfolio",
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
                (
                    "title",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="title"
                    ),
                ),
                ("date_at", models.DateTimeField(auto_now_add=True)),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("stocks", models.ManyToManyField(to="investment.company")),
            ],
        ),
    ]
