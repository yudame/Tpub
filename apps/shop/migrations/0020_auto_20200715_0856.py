# Generated by Django 3.0.7 on 2020-07-15 08:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0005_auto_20200714_0809'),
        ('shop', '0019_shop_gramables'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalshop',
            name='square_logo_src',
        ),
        migrations.RemoveField(
            model_name='shop',
            name='square_logo_src',
        ),
        migrations.AddField(
            model_name='historicalshop',
            name='icon_image',
            field=models.ForeignKey(blank=True, db_constraint=False, help_text='version of the logo that fits in a small square', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='common.Image'),
        ),
        migrations.AddField(
            model_name='historicalshop',
            name='logo_image',
            field=models.ForeignKey(blank=True, db_constraint=False, help_text='if not square will be padded, like a social media profile pic', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='common.Image'),
        ),
        migrations.AddField(
            model_name='shop',
            name='icon_image',
            field=models.OneToOneField(blank=True, help_text='version of the logo that fits in a small square', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='shop_as_icon', to='common.Image'),
        ),
        migrations.AddField(
            model_name='shop',
            name='logo_image',
            field=models.OneToOneField(blank=True, help_text='if not square will be padded, like a social media profile pic', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='shop_as_logo', to='common.Image'),
        ),
    ]
