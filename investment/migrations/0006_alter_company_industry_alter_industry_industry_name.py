# Generated by Django 4.1.7 on 2023-04-17 11:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("investment", "0005_exchange_securitytype_alter_commodity_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="company",
            name="industry",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="investment.industry",
            ),
        ),
        migrations.AlterField(
            model_name="industry",
            name="industry_name",
            field=models.CharField(max_length=50, verbose_name="industry_name"),
        ),
    ]