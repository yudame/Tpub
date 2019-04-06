# Generated by Django 2.1.2 on 2019-04-06 17:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('trello', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_anonymous', models.BooleanField(default=False)),
                ('authored_at', models.DateTimeField(blank=True, null=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('published_at', models.DateTimeField(blank=True, null=True)),
                ('edited_at', models.DateTimeField(blank=True, null=True)),
                ('unpublished_at', models.DateTimeField(blank=True, null=True)),
                ('trello_card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trello.Card')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('parent_blog', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.Blog')),
                ('trello_board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trello.Board')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('description', models.TextField(blank=True, default='')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]