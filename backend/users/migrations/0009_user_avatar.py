# Generated by Django 3.2.6 on 2021-08-14 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_remove_team_verified'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Avatar Image'),
        ),
    ]
