# Generated by Django 4.1.7 on 2023-04-17 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("investment", "0008_alter_reportperiod_options_alter_sector_sector_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="companyratios",
            name="date_at_findata",
            field=models.DateField(null=True, verbose_name="date_at"),
        ),
    ]
