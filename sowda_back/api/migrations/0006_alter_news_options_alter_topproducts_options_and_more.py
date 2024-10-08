# Generated by Django 5.0.7 on 2024-08-22 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_imagetop_top'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['-created', 'checked'], 'verbose_name': 'Habar', 'verbose_name_plural': 'Habarlar'},
        ),
        migrations.AlterModelOptions(
            name='topproducts',
            options={'ordering': ['-created', 'checked'], 'verbose_name': 'Saýlanan', 'verbose_name_plural': 'Saýlananlar'},
        ),
        migrations.AlterField(
            model_name='imagetop',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Döredilen wagty'),
        ),
        migrations.AlterField(
            model_name='news',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Döredilen wagty'),
        ),
        migrations.AlterField(
            model_name='topproducts',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Döredilen wagty'),
        ),
    ]
