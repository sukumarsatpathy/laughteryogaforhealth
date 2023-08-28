# Generated by Django 4.1.7 on 2023-05-02 05:48

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, unique=True, verbose_name='Title')),
                ('slug', models.SlugField(allow_unicode=True, max_length=500, unique=True, verbose_name='Slug')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Message')),
                ('image', models.ImageField(null=True, upload_to='blog/%Y/%m/%d/', verbose_name='Image')),
                ('status', models.CharField(choices=[('Published', 'Published'), ('Draft', 'Draft')], default='Published', max_length=10, verbose_name='Status')),
                ('views', models.IntegerField(default=0, verbose_name='Views')),
                ('submission_date', models.DateTimeField(auto_now_add=True, verbose_name='Submission Date')),
                ('meta_title', models.CharField(blank=True, max_length=60, null=True, verbose_name='Meta Title')),
                ('meta_description', models.CharField(blank=True, max_length=160, null=True, verbose_name='Meta Description')),
                ('meta_keywords', models.CharField(blank=True, max_length=200, null=True, verbose_name='Meta Keywords')),
            ],
            options={
                'verbose_name': 'Blog',
                'verbose_name_plural': 'Blogs',
                'db_table': 'blog-list',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(max_length=500, verbose_name='Full Name')),
                ('email', models.EmailField(max_length=500, verbose_name='Email')),
                ('message', models.TextField(verbose_name='Message')),
                ('ip', models.CharField(blank=True, max_length=20, verbose_name='IP Address')),
                ('status', models.BooleanField(default=True, verbose_name='Status')),
                ('submission_date', models.DateTimeField(auto_now_add=True, verbose_name='Submission Date')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogs.blog')),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
                'db_table': 'comment-list',
            },
        ),
    ]
