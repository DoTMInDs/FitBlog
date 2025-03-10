# Generated by Django 5.1.5 on 2025-02-07 20:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_articlecomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepostmodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/', validators=[django.core.validators.FileExtensionValidator(['png', 'jpg', 'jpeg', 'jfif'])]),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/', validators=[django.core.validators.FileExtensionValidator(['png', 'jpg', 'jpeg', 'jfif'])]),
        ),
    ]
