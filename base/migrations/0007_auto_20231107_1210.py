# Generated by Django 3.2.22 on 2023-11-07 06:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_auto_20231107_1208'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='advancedtravelplan',
            options={'verbose_name': 'Advanced Travel Plan'},
        ),
        migrations.AlterModelOptions(
            name='expense',
            options={'verbose_name': 'Actual Travel Plan'},
        ),
        migrations.AlterModelOptions(
            name='flightbudget',
            options={'verbose_name': 'Flight Budget'},
        ),
        migrations.AlterModelOptions(
            name='opebudget',
            options={'verbose_name': 'OPE Budget'},
        ),
        migrations.AlterModelOptions(
            name='travelbudget',
            options={'verbose_name': 'Travel Budget'},
        ),
    ]