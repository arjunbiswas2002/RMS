# Generated by Django 4.2.7 on 2023-11-16 10:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resto', '0004_remove_booking_time_alter_booking_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='date',
        ),
    ]