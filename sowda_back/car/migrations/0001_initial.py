# Generated by Django 4.2.9 on 2024-06-25 13:11

import car.models
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('api', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Awtoulag kategoriýa',
                'verbose_name_plural': 'Awtoulag kategoriýalar',
            },
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('author', models.CharField(max_length=255, null=True)),
                ('phone', models.CharField(max_length=100, null=True)),
                ('img1', models.ImageField(null=True, upload_to=car.models.image_add_car)),
                ('img2', models.ImageField(null=True, upload_to=car.models.image_add_car)),
                ('img3', models.ImageField(null=True, upload_to=car.models.image_add_car)),
                ('img4', models.ImageField(null=True, upload_to=car.models.image_add_car)),
                ('img5', models.ImageField(null=True, upload_to=car.models.image_add_car)),
                ('text', tinymce.models.HTMLField()),
                ('created', models.DateField(auto_now_add=True)),
                ('checked', models.BooleanField(default=False)),
                ('price', models.CharField(max_length=100, null=True)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.address')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car.carcategory')),
            ],
            options={
                'verbose_name': 'Awotulag',
                'verbose_name_plural': 'Awtoulaglar',
            },
        ),
    ]