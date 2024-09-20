# Generated by Django 5.0.7 on 2024-08-05 20:45

import django.db.models.deletion
import elin.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elin', '0002_alter_elin_phone_alter_elin_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='elin',
            old_name='img1',
            new_name='img',
        ),
        migrations.RemoveField(
            model_name='elin',
            name='img2',
        ),
        migrations.RemoveField(
            model_name='elin',
            name='img3',
        ),
        migrations.RemoveField(
            model_name='elin',
            name='img4',
        ),
        migrations.RemoveField(
            model_name='elin',
            name='img5',
        ),
        migrations.CreateModel(
            name='ImageElin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(null=True, upload_to=elin.models.image_add_elin, verbose_name='Surat')),
                ('created', models.DateField(auto_now_add=True, null=True, verbose_name='Döredilen wagty')),
                ('elin', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='elin.elin', verbose_name='Haryt')),
            ],
            options={
                'verbose_name': 'Elin surat',
                'verbose_name_plural': 'Elin suratlar',
            },
        ),
    ]