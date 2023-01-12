# Generated by Django 4.0.5 on 2022-06-16 16:21

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
            name='Notes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='İçerik')),
                ('content', models.TextField(verbose_name='içerik')),
                ('created_date', models.DateTimeField(auto_now=True, verbose_name='oluşturma tarihi')),
                ('motes_show', models.BooleanField(default=True)),
                ('deleted_date', models.DateTimeField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Yazar')),
            ],
        ),
    ]