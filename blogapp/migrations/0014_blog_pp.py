# Generated by Django 3.2.7 on 2021-10-12 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0013_remove_blog_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='pp',
            field=models.CharField(default=11, max_length=15),
            preserve_default=False,
        ),
    ]
