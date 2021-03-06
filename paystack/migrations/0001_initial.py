# Generated by Django 2.2 on 2021-12-12 11:26

import uuid

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="TransactionLog",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("uuid", models.UUIDField(default=uuid.uuid4, unique=True)),
                (
                    "charge_type",
                    models.CharField(
                        choices=[
                            ("GATEWAY_PURCHASE", "Gateway Purchase"),
                            ("TRANSFER", "Transfer"),
                        ],
                        max_length=30,
                    ),
                ),
                ("amount", models.FloatField(max_length=19)),
                ("currency", models.CharField(max_length=5)),
                ("txRef", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "payment_date_time",
                    models.DateTimeField(blank=True, max_length=100, null=True),
                ),
                ("status", models.CharField(blank=True, max_length=50, null=True)),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PayStackCustomer",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("email", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "authorization_code",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("card_type", models.CharField(blank=True, max_length=10, null=True)),
                ("last4", models.CharField(blank=True, max_length=4, null=True)),
                ("exp_month", models.CharField(blank=True, max_length=10, null=True)),
                ("exp_year", models.CharField(blank=True, max_length=10, null=True)),
                ("bin", models.CharField(blank=True, max_length=10, null=True)),
                ("bank", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "account_name",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
