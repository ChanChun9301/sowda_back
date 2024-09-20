# Generated by Django 5.0.7 on 2024-08-05 20:45

import django.db.models.deletion
import other.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('other', '0002_alter_other_phone_alter_other_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='other',
            old_name='img1',
            new_name='img',
        ),
        migrations.RemoveField(
            model_name='other',
            name='img2',
        ),
        migrations.RemoveField(
            model_name='other',
            name='img3',
        ),
        migrations.RemoveField(
            model_name='other',
            name='img4',
        ),
        migrations.RemoveField(
            model_name='other',
            name='img5',
        ),
        migrations.CreateModel(
            name='ImageOther',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(null=True, upload_to=other.models.image_add_beyleki, verbose_name='Surat')),
                ('created', models.DateField(auto_now_add=True, null=True, verbose_name='Döredilen wagty')),
                ('other', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='other.other', verbose_name='Haryt')),
            ],
            options={
                'verbose_name': 'Beyleki surat',
                'verbose_name_plural': 'Beyleki suratlar',
            },
        ),
    ]