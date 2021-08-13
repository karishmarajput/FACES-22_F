# Generated by Django 3.2.6 on 2021-08-12 20:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0004_team_verified'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_code', models.CharField(default=uuid.uuid4, max_length=36, unique=True, verbose_name='Transaction Code')),
                ('transaction_id', models.CharField(max_length=36, verbose_name='Transactions Id')),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Amount')),
                ('verified', models.BooleanField(default=False, verbose_name='Verified')),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Timestamp')),
                ('events', models.ManyToManyField(related_name='transactions', to='events.Event')),
                ('teams', models.ManyToManyField(related_name='transactions', to='users.Team')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
