# Generated by Django 5.0 on 2024-09-29 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consulta', '0004_client_cirgury_client_cook_client_family_sick_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='medication',
            options={'verbose_name': 'Medicamento/Suplemento', 'verbose_name_plural': 'Medicamentos/Suplementos'},
        ),
        migrations.AlterField(
            model_name='medication',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Medicamento/Suplemento'),
        ),
    ]
