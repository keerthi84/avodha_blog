# Generated by Django 3.2.7 on 2021-10-12 14:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blogapp', '0009_auto_20211012_1939'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='post',
            field=models.ForeignKey(default=10, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blog',
            name='author',
            field=models.CharField(max_length=50),
        ),
    ]
