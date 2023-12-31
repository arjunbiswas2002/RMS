# Generated by Django 4.2.7 on 2023-11-21 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resto', '0017_rename_your_field_contact_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='message',
            new_name='content',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='email',
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AddField(
            model_name='contact',
            name='Email',
            field=models.EmailField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]
