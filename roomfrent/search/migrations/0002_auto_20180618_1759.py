# Generated by Django 2.0.6 on 2018-06-18 17:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ownerinfo',
            name='email',
        ),
        migrations.RemoveField(
            model_name='ownerinfo',
            name='name',
        ),
        migrations.RemoveField(
            model_name='ownerinfo',
            name='owner_password',
        ),
        migrations.AddField(
            model_name='ownerinfo',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]