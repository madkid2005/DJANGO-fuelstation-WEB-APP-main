# Generated by Django 5.0.6 on 2024-06-28 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inspections', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fuelstation',
            name='no_gas_nozzles',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fuelstation',
            name='no_gasoline_nozzles',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
