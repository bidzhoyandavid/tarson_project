# Generated by Django 4.1.7 on 2023-04-17 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("investment", "0006_alter_company_industry_alter_industry_industry_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="industry",
            name="industry_name",
            field=models.CharField(max_length=100, verbose_name="industry_name"),
        ),
    ]
