# Generated by Django 4.2.9 on 2024-10-15 09:58

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import logist.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LogistCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Logistika kategoriýa',
                'verbose_name_plural': 'Logistika kategoriýalar',
            },
        ),
        migrations.CreateModel(
            name='Logist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('author', models.CharField(max_length=8, null=True)),
                ('where', models.CharField(max_length=20, null=True)),
                ('nirden', models.CharField(max_length=20, null=True)),
                ('last_date', models.DateField(null=True)),
                ('bring', models.BooleanField(default=False)),
                ('vip', models.BooleanField(default=False)),
                ('phone', models.IntegerField(null=True)),
                ('img', models.ImageField(null=True, upload_to=logist.models.image_add_logist)),
                ('text', ckeditor.fields.RichTextField(null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('checked', models.BooleanField(default=False)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.address')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='logist.logistcategory')),
            ],
            options={
                'verbose_name': 'Logistika',
                'verbose_name_plural': 'Logistikalar',
                'ordering': ['checked', '-created'],
            },
        ),
        migrations.CreateModel(
            name='ImageLogist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(null=True, upload_to=logist.models.images_add_logist, verbose_name='Surat')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Döredilen wagty')),
                ('logist', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='logist.logist', verbose_name='Haryt')),
            ],
            options={
                'verbose_name': 'Logistika surat',
                'verbose_name_plural': 'Logistika suratlar',
                'ordering': ['-created'],
            },
        ),
    ]
