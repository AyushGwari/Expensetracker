# Generated by Django 3.2.22 on 2023-11-07 06:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_auto_20231106_1517'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='advancedtravelplan',
            options={'verbose_name': 'Advanced Travel Plans'},
        ),
        migrations.AlterModelOptions(
            name='employee',
            options={'verbose_name': 'Employee'},
        ),
        migrations.AlterModelOptions(
            name='expense',
            options={'verbose_name': 'Actual Travel Plans'},
        ),
        migrations.AlterModelOptions(
            name='flightbudget',
            options={'verbose_name': 'Flight Budgets'},
        ),
        migrations.AlterModelOptions(
            name='opebudget',
            options={'verbose_name': 'OPE Budgets'},
        ),
        migrations.AlterModelOptions(
            name='travelbudget',
            options={'verbose_name': 'Travel Budgets'},
        ),
    ]