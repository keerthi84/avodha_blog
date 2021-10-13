# Generated by Django 3.2.7 on 2021-10-12 15:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blogapp', '0015_auto_20211012_2031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True),
        ),
    ]