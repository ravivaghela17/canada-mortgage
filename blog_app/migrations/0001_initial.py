# Generated by Django 3.1.7 on 2021-04-06 00:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_title', models.CharField(max_length=250)),
                ('slug', models.SlugField(unique=True)),
                ('sub_title', models.CharField(max_length=500)),
                ('body', models.CharField(max_length=3000)),
                ('blog_image', models.FileField(blank=True, upload_to='blog_image')),
                ('created_date_time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
