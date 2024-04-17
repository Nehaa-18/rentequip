# Generated by Django 4.1.5 on 2024-02-09 04:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0018_remove_product_company"),
    ]

    operations = [
        migrations.CreateModel(
            name="Driver",
            fields=[
                ("driver_d", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
                ("license_number", models.CharField(max_length=20)),
                ("date_of_birth", models.DateField()),
                ("address", models.CharField(max_length=255)),
                ("phone_number", models.CharField(max_length=20)),
                ("email", models.EmailField(max_length=254)),
            ],
        ),
    ]