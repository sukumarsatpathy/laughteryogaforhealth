# Generated by Django 4.1.7 on 2023-05-04 11:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='fb_url',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='gh_url',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='tw_url',
        ),
    ]
