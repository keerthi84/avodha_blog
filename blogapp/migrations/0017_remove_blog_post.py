# Generated by Django 3.2.7 on 2021-10-12 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0016_alter_blog_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='post',
        ),
    ]
