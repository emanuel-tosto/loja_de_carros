# Generated by Django 4.1.4 on 2023-01-01 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("vendedores", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Carro",
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
                ("marca", models.CharField(max_length=100)),
                (
                    "categoria",
                    models.CharField(
                        choices=[("Novo", "Novo"), ("Usado", "Usado")], max_length=50
                    ),
                ),
                ("image_main", models.ImageField(blank=True, upload_to="images")),
                ("image1", models.ImageField(blank=True, upload_to="images")),
                ("image2", models.ImageField(blank=True, upload_to="images")),
                ("image3", models.ImageField(blank=True, upload_to="images")),
                ("image4", models.ImageField(blank=True, upload_to="images")),
                ("image5", models.ImageField(blank=True, upload_to="images")),
                ("milhagem", models.IntegerField(blank=True, null=True)),
                (
                    "CAMBIO",
                    models.CharField(
                        choices=[("Manual", "Manual"), ("Automatica", "Automatica")],
                        max_length=50,
                    ),
                ),
                (
                    "ano",
                    models.IntegerField(
                        choices=[
                            (2005, 2005),
                            (2006, 2006),
                            (2007, 2007),
                            (2008, 2008),
                            (2009, 2009),
                            (2010, 2010),
                            (2011, 2011),
                            (2012, 2012),
                            (2013, 2013),
                            (2014, 2014),
                            (2015, 2015),
                            (2016, 2016),
                            (2017, 2017),
                            (2018, 2018),
                            (2019, 2019),
                            (2020, 2020),
                            (2021, 2021),
                            (2022, 2022),
                            (2023, 2023),
                        ],
                        default=2023,
                        verbose_name="year",
                    ),
                ),
                ("forca", models.IntegerField()),
                ("combustivel", models.IntegerField()),
                ("preco", models.IntegerField()),
                ("descricao", models.TextField()),
                ("data", models.DateField(auto_now_add=True)),
                (
                    "vendedor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="vendedores.vendedor",
                    ),
                ),
            ],
        ),
    ]