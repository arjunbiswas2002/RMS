# Generated by Django 4.2.7 on 2023-11-16 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resto', '0003_booking_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='time',
        ),
        migrations.AlterField(
            model_name='booking',
            name='date',
            field=models.DateField(),
        ),
    ]
