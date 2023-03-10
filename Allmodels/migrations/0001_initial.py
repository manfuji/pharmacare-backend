# Generated by Django 4.1.2 on 2022-12-14 11:14

import Allmodels.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Categories",
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
                ("catName", models.CharField(max_length=250)),
                ("createdAt", models.DateTimeField(auto_now=True)),
                ("updatedAt", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="Profile",
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
                ("country", models.CharField(blank=True, max_length=250, null=True)),
                ("city", models.CharField(blank=True, max_length=250, null=True)),
                ("address", models.TextField(blank=True, null=True)),
                ("zipcode", models.CharField(blank=True, max_length=50, null=True)),
                (
                    "profileImage",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to=Allmodels.models.Profile.upload_location,
                        verbose_name="Image",
                    ),
                ),
                ("created", models.DateTimeField(auto_now=True)),
                ("updatedAt", models.DateTimeField(auto_now=True)),
                (
                    "profileUser",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Product",
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
                ("productName", models.CharField(max_length=250)),
                ("description", models.TextField()),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("AVAILABLE", "AVAILABLE"),
                            ("UNAVAILABLE", "UNAVAILABLE"),
                        ],
                        default="AVAILABLE",
                        max_length=50,
                    ),
                ),
                ("productPrice", models.DecimalField(decimal_places=2, max_digits=10)),
                ("category", models.CharField(max_length=250)),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to=Allmodels.models.Product.upload_location,
                        verbose_name="Image",
                    ),
                ),
                ("slug", models.SlugField()),
                ("discount", models.CharField(default="20", max_length=50)),
                ("createdAt", models.DateTimeField(auto_now=True)),
                ("updatedAt", models.DateTimeField(auto_now=True)),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Order",
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
                ("quantity", models.CharField(max_length=250)),
                ("amount", models.DecimalField(decimal_places=2, max_digits=10)),
                ("orderTime", models.DateTimeField(auto_now=True)),
                (
                    "payment",
                    models.CharField(
                        choices=[
                            ("PAID", "PAID"),
                            ("PENDING", "PENDING"),
                            ("PAYONDELIVERY", "PAYONDELIVERY"),
                        ],
                        default="PENDING",
                        max_length=50,
                    ),
                ),
                ("orderComplete", models.BooleanField(default=False)),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "productId",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Allmodels.product",
                    ),
                ),
            ],
        ),
    ]
