# Generated by Django 2.2.8 on 2019-12-08 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Variable",
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
                ("name", models.SlugField(max_length=64, unique=True)),
                ("value_binary", models.BinaryField()),
            ],
            options={"ordering": ("name",),},
        ),
    ]
