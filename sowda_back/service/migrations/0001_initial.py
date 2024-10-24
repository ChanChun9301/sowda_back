# Generated by Django 4.2.9 on 2024-10-15 09:58

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import service.models


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
                ('phone', models.IntegerField(null=True)),
                ('img', models.ImageField(null=True, upload_to=service.models.image_add_hyzmat)),
                ('text', ckeditor.fields.RichTextField(null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('checked', models.BooleanField(default=False)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.address')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.servicecategory')),
            ],
            options={
                'verbose_name': 'Hyzmatlar',
                'verbose_name_plural': 'Hyzmatlar',
                'ordering': ['-created', 'checked'],
            },
        ),
        migrations.CreateModel(
            name='ImageService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(null=True, upload_to=service.models.image_add_hyzmat, verbose_name='Surat')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Döredilen wagty')),
                ('service', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='service.service', verbose_name='Haryt')),
            ],
            options={
                'verbose_name': 'Hyzmat surat',
                'verbose_name_plural': 'Hyzmat suratlar',
                'ordering': ['created'],
            },
        ),
    ]
