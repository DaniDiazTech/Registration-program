# Generated by Django 3.1.8 on 2021-04-21 23:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time in wich the object was modified', verbose_name='Created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time in which the object was modified', verbose_name='Modified at')),
                ('name', models.CharField(max_length=120, verbose_name='Student name')),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time in wich the object was modified', verbose_name='Created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time in which the object was modified', verbose_name='Modified at')),
                ('name', models.CharField(max_length=75, unique=True, verbose_name='A classroom is the way students check their asistance')),
                ('slug', models.SlugField(unique=True)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
    ]