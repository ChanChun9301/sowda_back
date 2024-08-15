# Generated by Django 5.0.7 on 2024-07-25 17:54

import django.db.models.deletion
import other.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OtherCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Beýleki kategoriýa',
                'verbose_name_plural': 'Beýleki kategoriýalar',
            },
        ),
        migrations.CreateModel(
            name='Other',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('author', models.CharField(max_length=8, null=True)),
                ('phone', models.CharField(max_length=8, null=True)),
                ('img1', models.ImageField(null=True, upload_to=other.models.image_add_beyleki)),
                ('img2', models.ImageField(null=True, upload_to=other.models.image_add_beyleki)),
                ('img3', models.ImageField(null=True, upload_to=other.models.image_add_beyleki)),
                ('img4', models.ImageField(null=True, upload_to=other.models.image_add_beyleki)),
                ('img5', models.ImageField(null=True, upload_to=other.models.image_add_beyleki)),
                ('text', models.TextField(blank=True)),
                ('created', models.DateField(auto_now_add=True)),
                ('checked', models.BooleanField(default=False)),
                ('price', models.CharField(max_length=100, null=True)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.address')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='other.othercategory')),
            ],
            options={
                'verbose_name': 'Beylekiler',
                'verbose_name_plural': 'Beylekiler',
            },
        ),
    ]
