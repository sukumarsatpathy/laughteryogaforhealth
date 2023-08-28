# Generated by Django 4.1.7 on 2023-05-02 05:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('first_name', models.CharField(max_length=50, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=50, verbose_name='Last Name')),
                ('username', models.CharField(max_length=50, unique=True, verbose_name='Username')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='Email')),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('last_login', models.DateTimeField(auto_now_add=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('is_superadmin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=50, verbose_name='Contact No')),
                ('designation', models.CharField(max_length=50, verbose_name='Designation')),
                ('company_name', models.CharField(blank=True, max_length=50, verbose_name='Company Name')),
                ('address_line_1', models.CharField(blank=True, max_length=100, verbose_name='Address 1')),
                ('address_line_2', models.CharField(blank=True, max_length=100, verbose_name='Address 2')),
                ('picture', models.ImageField(blank=True, upload_to='picture/%Y/%m/%d/', verbose_name='Picture')),
                ('fb_url', models.URLField(blank=True, max_length=100, null=True, verbose_name='Facebook')),
                ('tw_url', models.URLField(blank=True, max_length=100, null=True, verbose_name='Twitter')),
                ('gh_url', models.URLField(blank=True, max_length=100, null=True, verbose_name='GitHub')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='Modified Date')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]