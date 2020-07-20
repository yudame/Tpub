# Generated by Django 3.0.7 on 2020-07-20 06:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0021_auto_20200718_0819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='shop', to=settings.AUTH_USER_MODEL),
        ),
    ]