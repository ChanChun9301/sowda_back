# Generated by Django 4.2.9 on 2024-07-02 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='author',
            field=models.CharField(max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='phone',
            field=models.CharField(max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='text',
            field=models.TextField(blank=True),
        ),
    ]
