# Generated by Django 4.2.7 on 2023-12-02 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resto', '0027_alter_booking_phonenumber'),
    ]

    operations = [
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='profile_pics/')),
            ],
        ),
    ]
