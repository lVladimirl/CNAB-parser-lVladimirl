# Generated by Django 4.1.2 on 2022-11-24 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Cnab",
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
                ("type", models.CharField(max_length=1)),
                ("date", models.DateField()),
                ("value", models.IntegerField()),
                ("hour", models.TimeField()),
            ],
        ),
    ]
