# Generated by Django 5.0.7 on 2024-07-25 17:54

import django.db.models.deletion
import service.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Hyzmat kategoriýa',
                'verbose_name_plural': 'Hyzmat kategoriýalar',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('author', models.CharField(max_length=8, null=True)),
                ('phone', models.CharField(max_length=8, null=True)),
                ('img1', models.ImageField(null=True, upload_to=service.models.image_add_hyzmat)),
                ('img2', models.ImageField(null=True, upload_to=service.models.image_add_hyzmat)),
                ('img3', models.ImageField(null=True, upload_to=service.models.image_add_hyzmat)),
                ('img4', models.ImageField(null=True, upload_to=service.models.image_add_hyzmat)),
                ('img5', models.ImageField(null=True, upload_to=service.models.image_add_hyzmat)),
                ('text', models.TextField(blank=True)),
                ('created', models.DateField(auto_now_add=True)),
                ('checked', models.BooleanField(default=False)),
                ('price', models.CharField(max_length=100, null=True)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.address')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.servicecategory')),
            ],
            options={
                'verbose_name': 'Hyzmatlar',
                'verbose_name_plural': 'Hyzmatlar',
            },
        ),
    ]
