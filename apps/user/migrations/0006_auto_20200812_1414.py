# Generated by Django 3.0.7 on 2020-08-12 14:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_user_pushover_device_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='pushover_key',
            new_name='pushover_user_key',
        ),
    ]
