# Generated by Django 3.1.7 on 2021-04-04 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term', models.CharField(max_length=200)),
                ('rate', models.DecimalField(decimal_places=4, max_digits=5)),
                ('apr', models.DecimalField(decimal_places=4, max_digits=5, null=True)),
            ],
        ),
    ]
