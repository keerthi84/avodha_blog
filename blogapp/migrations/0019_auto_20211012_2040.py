# Generated by Django 3.2.7 on 2021-10-12 15:10

import ckeditor.fields
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0018_auto_20211012_2038'),
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('title_tag', models.CharField(max_length=225)),
                ('author', models.CharField(max_length=50)),
                ('date', models.DateField(default=datetime.date.today)),
                ('img', models.ImageField(upload_to='images')),
                ('body', ckeditor.fields.RichTextField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='blogg',
        ),
    ]
