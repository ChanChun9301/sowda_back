# Generated by Django 4.2.9 on 2024-06-25 13:12

import api.models
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CarouselImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('img', models.ImageField(null=True, upload_to='carousel')),
            ],
        ),
        migrations.CreateModel(
            name='NewsCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Habar kategoriýa',
                'verbose_name_plural': 'Habar kategoriýalar',
            },
        ),
        migrations.CreateModel(
            name='TopProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('category', models.CharField(max_length=100, null=True)),
                ('author', models.CharField(max_length=255, null=True)),
                ('phone', models.CharField(max_length=100, null=True)),
                ('img1', models.ImageField(default='/static/', null=True, upload_to=api.models.image_add_top)),
                ('img2', models.ImageField(null=True, upload_to=api.models.image_add_top)),
                ('img3', models.ImageField(null=True, upload_to=api.models.image_add_top)),
                ('img4', models.ImageField(null=True, upload_to=api.models.image_add_top)),
                ('img5', models.ImageField(null=True, upload_to=api.models.image_add_top)),
                ('text', models.TextField(blank=True)),
                ('created', models.DateField(auto_now_add=True)),
                ('checked', models.BooleanField(default=False)),
                ('price', models.CharField(max_length=100, null=True)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.address')),
            ],
            options={
                'verbose_name': 'Saýlanan',
                'verbose_name_plural': 'Saýlananlar',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('author', models.CharField(max_length=150, null=True)),
                ('img', models.ImageField(null=True, upload_to=api.models.image_add_habar)),
                ('text', tinymce.models.HTMLField()),
                ('created', models.DateField(auto_now_add=True)),
                ('checked', models.BooleanField(default=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.newscategory')),
            ],
            options={
                'verbose_name': 'Habar',
                'verbose_name_plural': 'Habarlar',
            },
        ),
        migrations.CreateModel(
            name='UserProd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('author', models.CharField(max_length=23, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Ulanyjy',
                'verbose_name_plural': 'Ulanyjylar',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
