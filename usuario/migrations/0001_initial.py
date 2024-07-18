# Generated by Django 4.2.13 on 2024-07-18 20:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Usuario",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("enabled", models.BooleanField(default=True, verbose_name="Ativo")),
                ("deleted", models.BooleanField(default=False)),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("updated_on", models.DateTimeField(auto_now=True)),
                (
                    "cpf",
                    models.CharField(
                        blank=True,
                        max_length=11,
                        null=True,
                        unique=True,
                        verbose_name="CPF",
                    ),
                ),
                ("nome", models.CharField(max_length=300, verbose_name="Nome")),
                (
                    "email",
                    models.EmailField(
                        max_length=254, unique=True, verbose_name="E-mail"
                    ),
                ),
                (
                    "telefone",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="Telefone"
                    ),
                ),
                (
                    "token",
                    models.TextField(
                        blank=True, editable=False, null=True, verbose_name="Token"
                    ),
                ),
                (
                    "firebase",
                    models.TextField(
                        blank=True, null=True, verbose_name="Token Firebase"
                    ),
                ),
                (
                    "access_token",
                    models.TextField(
                        blank=True, null=True, verbose_name="Access Token"
                    ),
                ),
                (
                    "id_token",
                    models.TextField(blank=True, null=True, verbose_name="ID Token"),
                ),
                ("latitude", models.FloatField(default=0.0, verbose_name="Latitude")),
                ("longitude", models.FloatField(default=0.0, verbose_name="Longitude")),
                (
                    "endereco",
                    models.TextField(
                        blank=True, null=True, verbose_name="Endereço Residencial"
                    ),
                ),
                (
                    "django_user",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Django User",
                    ),
                ),
            ],
            options={
                "verbose_name": "Usuário",
                "verbose_name_plural": "Usuários",
            },
        ),
    ]
