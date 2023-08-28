# Generated by Django 4.1.7 on 2023-03-15 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(max_length=500, null=True, verbose_name='Full Name')),
                ('email', models.EmailField(max_length=500, null=True, verbose_name='Email')),
                ('contact', models.CharField(max_length=20, null=True, verbose_name='Contact')),
                ('country', models.CharField(max_length=100, null=True, verbose_name='Country')),
                ('message', models.TextField(null=True, verbose_name='Message')),
                ('submitted_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
            ],
            options={
                'verbose_name': 'Invite',
                'verbose_name_plural': 'Invite',
                'db_table': 'invite_list',
            },
        ),
    ]
