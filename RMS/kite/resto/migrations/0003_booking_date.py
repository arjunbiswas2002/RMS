# Generated by Django 4.2.7 on 2023-11-15 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resto', '0002_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='date',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=1),
            preserve_default=False,
        ),
    ]