# Generated by Django 3.2.6 on 2021-08-13 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20210813_1202'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='is_paid',
            field=models.BooleanField(default=False, verbose_name='Is Paid'),
        ),
        migrations.AlterField(
            model_name='team',
            name='is_verified',
            field=models.BooleanField(default=False, verbose_name='Is Verified'),
        ),
    ]
