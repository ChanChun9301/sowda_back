# Generated by Django 5.0.7 on 2024-08-22 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0003_rename_img1_service_img_remove_service_img2_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='imageservice',
            options={'ordering': ['created'], 'verbose_name': 'Hyzmat surat', 'verbose_name_plural': 'Hyzmat suratlar'},
        ),
        migrations.AlterModelOptions(
            name='service',
            options={'ordering': ['-created', 'checked'], 'verbose_name': 'Hyzmatlar', 'verbose_name_plural': 'Hyzmatlar'},
        ),
        migrations.AlterField(
            model_name='imageservice',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Döredilen wagty'),
        ),
        migrations.AlterField(
            model_name='service',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]