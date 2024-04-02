# Generated by Django 4.2.10 on 2024-03-11 11:55

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_addedmodel_img1_alter_addedmodel_img2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addedmodel',
            name='img1',
            field=models.ImageField(null=True, upload_to=api.models.image_add),
        ),
        migrations.AlterField(
            model_name='addedmodel',
            name='img2',
            field=models.ImageField(null=True, upload_to=api.models.image_add),
        ),
        migrations.AlterField(
            model_name='addedmodel',
            name='img3',
            field=models.ImageField(null=True, upload_to=api.models.image_add),
        ),
        migrations.AlterField(
            model_name='addedmodel',
            name='img4',
            field=models.ImageField(null=True, upload_to=api.models.image_add),
        ),
        migrations.AlterField(
            model_name='addedmodel',
            name='img5',
            field=models.ImageField(null=True, upload_to=api.models.image_add),
        ),
    ]
